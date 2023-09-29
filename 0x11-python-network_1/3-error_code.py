#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} URL")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"URLError: {e}")
