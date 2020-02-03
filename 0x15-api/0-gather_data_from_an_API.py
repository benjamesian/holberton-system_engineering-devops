#!/usr/bin/python3
"""
Under my umbrella
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'

    user_endpoint = '/users/{:s}'.format(argv[1])
    user_resp = requests.get(url + user_endpoint)
    user_json = user_resp.json()
    user_id = user_json.get('id')

    todo_resp = requests.get(url + '/todos', params={'userId': user_id})
    user_todos = todo_resp.json()
    completed_todos = list(filter(lambda x: x.get('completed', False),
                                  user_todos))

    print('Employee {:s} is done with tasks({:d}/{:d}):'.format(
        user_json.get('name'),
        len(completed_todos),
        len(user_todos)))
    for todo in completed_todos:
        print('\t {:s}'.format(todo.get('title')))
