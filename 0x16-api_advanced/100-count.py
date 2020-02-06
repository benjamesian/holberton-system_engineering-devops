#!/usr/bin/python3
"""
Check titles of hot posts in a subreddit.
"""

from requests import request

RAW_URL = 'http://www.reddit.com/r/{:s}/hot.json'


def count_words(subreddit, word_list, after='', counts={}):
    """Get the titles of the top ten hottest posts on a subreddit."""
    headers = {'User-Agent': 'py3'}
    url = RAW_URL.format(subreddit)
    params = {'limit': 100}
    if after:
        params['after'] = after

    resp = request('GET',
                   url,
                   headers=headers,
                   params=params,
                   allow_redirects=False,
                   timeout=10)
    if resp.status_code != 200:
        print()
        return

    data = resp.json().get('data', {})

    hot_titles = list(map(
        lambda x: x.get('data', {}).get('title'),
        data.get('children', {})))

    title_words = ' '.join(hot_titles).split(' ')
    for word in title_words:
        lower = word.lower()
        if lower in word_list:
            counts[lower] = counts.get(lower, 0) + 1

    if hot_titles:
        after = data.get('after', '')
        if after:
            return count_words(subreddit, word_list, after, counts)

    word_list.sort()
    word_list.sort(key=(lambda a: -counts.get(a, 0)))
    if word_list:
        for word in word_list:
            if word in counts:
                print('{:s}: {:d}'.format(word, counts[word]))
    else:
        print()
