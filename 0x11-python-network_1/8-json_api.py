#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user"""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    response = requests.post(url, data=payload)

    try:
        response = response.json()
        if response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
