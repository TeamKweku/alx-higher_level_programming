#!/usr/bin/python3
"""script that takes in a URL and an email, sends a
POST request to the passed URL with the email as a parameter"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    try:
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e}")
    except urllib.error.URLError as e:
        print(f"URLError: {e}")
