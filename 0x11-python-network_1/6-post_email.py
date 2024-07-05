#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
finally displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
