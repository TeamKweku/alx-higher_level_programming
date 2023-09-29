#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("\t-  type:", type(body))
print("\t-  content:", repr(body))
print("\t-  utf-8 content:", utf8_content)
