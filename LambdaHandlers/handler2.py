import json
import os

if __name__ == '__main__':
    return json.dumps({
        'data': os.environ.get('my_var'),
        'status': 'OK'
    })