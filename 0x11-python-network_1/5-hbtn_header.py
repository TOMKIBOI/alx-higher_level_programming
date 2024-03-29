#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
