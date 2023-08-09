#!/usr/bin/python3
"""
This script takes the URL and sends request to the URL 
and it displays the value of the variable X-Request-Id.
"""
import requests
import sys

def fetch_request_id(url):
    """
    Fetches the value of the X-Request-Id variable from
    the response header of a given URL.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable from
        the response header.

    Raises:
        requests.exceptions.RequestException: If an error
        occurs during the HTTP request.
    """
    response = requests.get(url)

    if response.status_code == 200:
        request_id = response.headers.get('X-Request-Id')
        return request_id
    else:
        raise requests.exceptions.RequestException(f"Error: {response.status_code}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a URL as a command-line argument.")
    else:
        url = sys.argv[1]
        try:
            request_id = fetch_request_id(url)
            print(f"X-Request-Id: {request_id}")
        except requests.exceptions.RequestException as e:
            print(e)
