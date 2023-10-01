#!/usr/bin/python3
"""A script that checks the last 10 commits of a github repo"""
import requests
import sys

def fetch_commits(repository, owner):
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f'Failed to fetch commits. Status code: {response.status_code}')
        print(response.text)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python script.py <repository_name> <owner_name>')
    else:
        repository_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(repository_name, owner_name)
