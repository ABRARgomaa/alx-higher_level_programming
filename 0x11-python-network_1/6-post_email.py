#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import requests
    import sys
    u = sys.argv[1]
    data = {'email': sys.argv[2]}
    with requests.post(u, data=data) as response:
        print(response.text)
