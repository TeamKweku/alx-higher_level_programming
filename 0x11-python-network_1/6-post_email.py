#!/usr/bin/python3
""" a Python script that takes a URL as argument """


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    response = requests.post(url, data=payload)

    print(response.text)
