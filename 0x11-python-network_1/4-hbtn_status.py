#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: ", end='')
    print(type(response.text))
    print("\t- content: ", end='')
    print(response.text)
