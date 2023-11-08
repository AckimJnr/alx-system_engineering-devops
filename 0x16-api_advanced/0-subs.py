#!/usr/bin/python3
"""
Module contains a function that retrieves the number of
subscribers for a sub redit
"""
import requests


def number_of_subscribers(subreddit):
    """
    @subreddit: the subreddit to be checked
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
