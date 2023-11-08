#!/usr/bin/python3
"""
Retrieve the top 10 comments of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    @subreddit: the subreddit to be checked
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)

    if response.status_code == 200:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts:
                title = post['data']['title']
                print(f"{title}")
        else:
            print(None)
    else:
        print(None)
