import requests

def handler(event, context):
    r = requests.get(
        'https://my.url/api/user',
        params={'email': event['body']['email']}
    )
    r.raise_for_status()

    return r.json()

if __name__ == '__main__':
    handler({'body': {'email': 'test@example.com'}}, None)