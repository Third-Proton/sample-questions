import json
from mylib import process_record

def handler(event, context):
    status_code = 200
    results = []
    for record in event['Records']:
        try:
            data = json.loads(record['body'])
            result = process_record(data)
            results.append(result)
        except Exception as e:
            results.append({
                'record_id': record['id'],
                'error': str(e)
            })
            status_code = 500

    return {
        'statusCode': status_code,
        'body': json.dumps(results)
    }
