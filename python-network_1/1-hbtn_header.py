#!/usr/bin/python3
"""
This script takes the URL and sends request to the URL 
and it displays the value of the variable X-Request-Id.
"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)

if response.status_code == 200:
    request_id = response.headers.get('X-Request-Id')
    print(f"X-Request-Id: {request_id}")
else:
    print("Error:", response.status_code)
