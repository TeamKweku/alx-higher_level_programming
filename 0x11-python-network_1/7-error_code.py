#!/usr/bin/python3
""" a Python script that takes a URL as argument """


if __name__ == "__main__":
    import requests
    import sys

    # if len(sys.argv) != 2:
    #     print(f"Usage: {sys.argv[0]} <URL>")
    #     sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    status = response.status_code

    if status < 400:
        print(response.text)
    else:
        print(f"Error code: {status}")
