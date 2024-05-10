#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_data = response.read().decode('utf-8')
            print(response_data)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
