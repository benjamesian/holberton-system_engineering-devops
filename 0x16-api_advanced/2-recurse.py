#!/usr/bin/python3
"""
Check titles of hot posts in a subreddit.
"""

from requests import request
from sys import argv

RAW_URL = 'http://reddit.com/r/{:s}/hot.json'


def recurse(subreddit, hot_list=[], after=''):
    """Get the titles of the top ten hottest posts on a subreddit."""
    headers = {'User-agent': 'py3'}
    url = RAW_URL.format(subreddit)
    params = {'limit': 100}
    if after:
        params['after'] = after
    resp = request('GET', url, headers=headers, params=params)
    if resp.status_code != 200:
        return hot_list or None
    data = resp.json().get('data', {})
    hot_posts = list(map(
        lambda x: x.get('data', {}).get('title'),
        data.get('children', {})))
    if not hot_posts:
        return hot_list or None
    hot_list.extend(hot_posts)
    after = data.get('after', '')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
