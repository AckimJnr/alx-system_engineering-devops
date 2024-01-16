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
        'User-Agent': 'advancedApi/1.0 (by /u/AckimJnr)'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
