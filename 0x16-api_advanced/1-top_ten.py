#!/usr/bin/python3
"""
Check titles of hot posts in a subreddit.
"""

import requests

RAW_URL = 'https://www.reddit.com/r/{:s}/hot.json'


def top_ten(subreddit):
    """Get the titles of the top ten hottest posts on a subreddit."""
    headers = {'User-Agent': ''}
    params = {'limit': 10}
    resp = requests.get(RAW_URL.format(subreddit),
                        headers=headers,
                        params=params,
                        allow_redirects=False,
                        timeout=10)
    if resp.status_code == 200:
        for post in resp.json().get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        print('None')
