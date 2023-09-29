#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL anddisplays
displays the valueofof the X-Request-Id """


if __name__ == "__main__":
    import sys
    import urllib.request

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} URL")
        sys.exit(1)

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_req_id = response.headers.get('X-Request-Id')
            if x_req_id:
                print(x_req_id)
    except urllib.error.HTTPError as e:
        print(f"HTTPError: {e}")
    except urllib.error.URLError as e:
        print(f"URLError: {e}")
