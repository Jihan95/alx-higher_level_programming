#!/usr/bin/python3
"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:')
print('    - type: ', end='')
print(type(html))
print('    - content: ', end='')
print(html)
print('    - utf8 content: ', end='')
encoding = response.headers.get_content_charset()
if encoding and 'utf-8' in encoding.lower():
    print('OK')
