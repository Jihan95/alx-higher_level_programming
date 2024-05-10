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
    print('    - type: ', end='')
    print(type(html))
    print('    - content: ', end='')
    print(html)
    print('    - utf8 content: ', end='')
    print(html.decode('utf-8'))
