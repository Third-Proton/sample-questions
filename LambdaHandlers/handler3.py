import boto3
import os
import requests
import urllib.parse


s3 = boto3.client('s3')
ssm = boto3.client('ssm')

nasa_api_key = ssm.get_parameter(
    Name=os.environ['NASA_API_KEY_PARAM_NAME'],
    WithDecryption=True
)['Parameter']['Value']

results_bucket_name = 'nasa-apod-query-results'


def handler(event, context):
    query_result_s3_urls = []

    query_params = event.get('nasa_api_query_params', {})
    if 'api_key' not in query_params:
        query_params['api_key'] = nasa_api_key

    r = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params=query_params
    )
    r.raise_for_status()

    # Example response:
    #
    # [
    #   {
    #     "copyright": "Betul Turksoy",
    #     "date": "2022-10-10",
    #     "explanation": "An analemma is that figure-8 curve you get when you mark the position of the Sun
    #                     at the same time each day for one year. But the trick to imaging an analemma of
    #                     the Moon is to wait bit longer. On average the Moon returns to the same position
    #                     in the sky about 50 minutes and 29 seconds later each day. So photograph the Moon
    #                     50 minutes 29 seconds later on successive days. Over one lunation or lunar month
    #                     it will trace out an analemma-like curve as the Moon's actual position wanders
    #                     due to its tilted and elliptical orbit. Since the featured image was taken over
    #                     two months, it actually shows a double lunar analemma.  Crescent lunar phases too
    #                     thin and faint to capture around the New moon are missing. The two months the
    #                     persistent astrophotographer chose were during a good stretch of weather during
    #                     July and August, and the location was Kayseri, Turkey",
    #     "hdurl": "https://apod.nasa.gov/apod/image/2210/LunarAnalemma_Turksoy_6755.jpg",
    #     "media_type": "image",
    #     "service_version": "v1",
    #     "title": "A Double Lunar Analemma over Turkey",
    #     "url": "https://apod.nasa.gov/apod/image/2210/LunarAnalemma_Turksoy_1080.jpg"
    #   }
    # ]
    photos = r.json()

    if not isinstance(photos, list):
        photos = [photos]

    for photo_info in photos:
        r = requests.get(photo_info['url'])
        r.raise_for_status()

        photo_filename = urllib.parse.unquote_plus(photo_info['url'].split('/')[-1])

        photo_file = f'/tmp/{photo_filename}'
        with open(photo_file, 'wb') as f:
            f.write(r.content)

        s3_key = f'{context.aws_request_id}/{photo_filename}'
        with open(photo_file) as f:
            s3.put_object(
                Body=f,
                Bucket=results_bucket_name,
                ContentType=r.headers.get('Content-Type'),
                Key=s3_key,
                Tagging=urllib.parse.urlencode(photo_info)
            )

        query_result_s3_urls.append(f's3://{results_bucket_name}/{s3_key}')

    return query_result_s3_urls
