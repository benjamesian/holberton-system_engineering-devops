#!/usr/bin/python3
"""
Check number of subscribers to a subreddit.
"""

from requests import request
from sys import argv

RAW_URL = 'http://reddit.com/r/{:s}/about.json'


def number_of_subscribers(subreddit):
    """Get the number of subscribers to a subreddit."""
    headers = {'User-agent': 'py3'}
    resp = request('GET', RAW_URL.format(subreddit), headers=headers)
    if resp.status_code != 200:
        return 0
    return resp.json().get('data', {}).get('subscribers', 0)
