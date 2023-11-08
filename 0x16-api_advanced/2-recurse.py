#!/usr/bin/python3
"""
queries the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    @subreddit: the subreddit
    @hot_list: the retrieved hot list
    @after: indication of pagination
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(
            url,
            headers={'User-Agent': 'Reddit API Example'},
            allow_redirects=False
            )

    if response.status_code == 200:
        query_string = f"limit=100&after={after}"
        url_base = f"https://www.reddit.com/r/{subreddit}/hot.json?"
        url = url_base + query_string
        response = requests.get(
                url,
                headers={'User-Agent': 'Reddit API Example'},
                allow_redirects=False
                )

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            hot_list.extend([post['data']['title'] for post in posts])

            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after=after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
