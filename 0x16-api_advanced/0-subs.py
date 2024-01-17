#!/usr/bin/python3
"""
Contains a function that retrieves the number of
subscribers for a subredit
"""
import requests


def number_of_subscribers(subreddit):
    """
    @subreddit: the subredit to be checked
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        'User-Agent': 'pyscript1.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data["data"]["subscribers"]

        return subs
    elif response.status_code == 404:
        return 0
    else:
        return 0
