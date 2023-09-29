#!/usr/bin/python3
""" a Python script that takes a URL as argument """


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    x_req_id = response.headers.get('X-Request-Id')
    print(x_req_id)
    # try:
    #     response.raise_for_status()
    # except requests.exceptions.HTTPError as e:
    #     print(f"Error: {e}")
    # else:
    #     x_req_id = response.headers.get('X-Request-Id')
    #     if x_req_id:
    #         print(x_req_id)
    #     else:
    #         print("X-Request-Id Not Found")
