#!/usr/bin/python3
"""
Write user todo info to a json.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    user_endpoint = '/users/{:s}'.format(argv[1])
    user_resp = requests.get(url + user_endpoint)
    user_json = user_resp.json()
    USER_ID = user_json.get('id')
    USERNAME = user_json.get('username')

    todo_resp = requests.get(url + '/todos', params={'userId': USER_ID})
    user_todos = todo_resp.json()

    d = {USER_ID: [{'task': todo.get('title'),
                    'completed': todo.get('completed', False),
                    'username': USERNAME} for todo in user_todos]}
    jsn = json.dumps(d)

    with open(str(USER_ID) + '.json', 'w') as f:
        f.write(jsn)
