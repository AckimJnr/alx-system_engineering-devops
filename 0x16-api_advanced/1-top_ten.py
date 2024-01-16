#!/usr/bin/python3
"""
Retrieve the top 10 comments of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    @subreddit: the subreddit to be checked
    Prints the subreddit if found
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url)

    if response.status_code == 200:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
        response = requests.get(url, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for i, post in enumerate(posts, start=1):
                title = post['data']['title']
                print(title)
        else:
            print("Fetch failed")
    else:
        print("None")
