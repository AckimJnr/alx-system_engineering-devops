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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        'User-Agent': 'pyscript1.0'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subs = data["data"]["subscribers"]

            return subs
        except KeyError:
            return 0
    elif response.status_code == 404:
        return 0
    else:
        return 0
