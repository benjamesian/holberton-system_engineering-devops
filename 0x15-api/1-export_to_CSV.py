#!/usr/bin/python3
"""
Write user todo info to a csv.
"""

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

    s = ''
    for todo in user_todos:
        TASK_COMPLETED_STATUS = todo.get('completed', False)
        TASK_TITLE = todo.get('title')
        s += '"{}","{}","{}","{}"\n'.format(
            USER_ID,
            USERNAME,
            TASK_COMPLETED_STATUS,
            TASK_TITLE)

    with open(str(USER_ID) + '.csv', 'w') as f:
        f.write(s)
