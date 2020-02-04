#!/usr/bin/python3
"""
Write all user todos to a json.
"""

from itertools import groupby
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    users_resp = requests.get(url + '/users')
    todos_resp = requests.get(url + '/todos')
    users = users_resp.json()
    todos = todos_resp.json()
    d = {}

    user_todos = {k: list(v) for k, v in groupby(
        todos, lambda todo: todo.get('userId'))}

    for user in users:
        USER_ID = user.get('id')
        d[USER_ID] = [{
            'username': user.get('username'),
            'task': todo.get('title'),
            'completed': todo.get('completed')
        } for todo in user_todos[USER_ID]]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(d, f)
