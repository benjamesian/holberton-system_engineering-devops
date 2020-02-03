#!/usr/bin/python3
"""
Write all user todos to a json.
"""

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    users_resp = requests.get(url + '/users')
    users_json = users_resp.json()
    d = {}
    for user in users_json:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        todo_resp = requests.get(url + '/todos', params={'userId': USER_ID})
        user_todos = todo_resp.json()
        d[USER_ID] = [{'username': USERNAME,
                       'task': todo.get('title'),
                       'completed': todo.get('completed', False)
                       } for todo in user_todos]

    jsn = json.dumps(d)

    with open('todo_all_employees.json', 'w') as f:
        f.write(jsn)
