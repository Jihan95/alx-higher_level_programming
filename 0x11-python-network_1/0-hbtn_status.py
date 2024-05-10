#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print('Body response:')
    print('\t- type: ', end='')
    print(type(html))
    print('\t- content: ', end='')
    print(html)
    print('\t- utf8 content: ', end='')
    print(html.decode('utf-8'))
