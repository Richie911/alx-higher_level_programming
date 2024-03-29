#!/usr/bin/python3
"""
Sends request to URL and displays the value of the variable X-Request-Id"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))