#!/usr/bin/python3
"""
Check titles of hot posts in a subreddit.
"""

import requests

RAW_URL = 'http://reddit.com/r/{:s}/hot.json'


def top_ten(subreddit):
    """Get the titles of the top ten hottest posts on a subreddit."""
    headers = {'User-agent': 'py3'}
    params = {'limit': 10}
    resp = requests.get(RAW_URL.format(subreddit),
                        headers=headers,
                        params=params,
                        allow_redirects=False)
    if resp.status_code != 200:
        print('None')
        return
    hot_posts = resp.json().get('data', {}).get('children', [])
    if not hot_posts:
        print('None')
    else:
        for post in hot_posts:
            print(post.get('data', {}).get('title'))
