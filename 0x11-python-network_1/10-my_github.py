#!/usr/bin/python3
"""
 a Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        user_name = sys.argv[1]
        password = sys.argv[2]
        url = "https://api.github.com/user"
        auth_header = {"Authorization": "Bearer {}".format(password)}
        response = requests.get(url, headers=auth_header)
        if response.status_code == 200:
            user_info = response.json()
            print(user_info['id'])
        else:
            print("None")
