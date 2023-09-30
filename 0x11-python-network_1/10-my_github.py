#!/usr/bin/python3
"""script that takes Github credentials and uses the Github API to display
id"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API endpoint to get user details
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    try:
        response_json = response.json()
        if "id" in response_json:
            print(response_json["id"])
        else:
            print("None")
    except ValueError:
        print("None")
