#!/usr/bin/python3
"""
Check titles of hot posts in a subreddit.
"""

from requests import request
from sys import argv

RAW_URL = 'http://reddit.com/r/{:s}/hot.json'


def top_ten(subreddit):
    """Get the titles of the top ten hottest posts on a subreddit."""
    headers = {'User-agent': 'py3'}
    resp = request('GET',
                   RAW_URL.format(subreddit), 
                   headers=headers,
                   allow_redirects=False)
    hot_posts = resp.json().get('data', {}).get('children', {})
    if resp.status_code != 200 or not hot_posts:
        print('None')
    for post in hot_posts[:10]:
        print(post.get('data', {}).get('title'))