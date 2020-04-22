import requests
import urllib.parse


class PlayfieldAPI:

    def __init__(self):
        pass

    def api_request(self, host, method, resource, function, data):

        if method.lower() == "get" and data is not None:
            url = f'http://{host}/api/v1/resources/{resource}/{function}/{urllib.parse.quote(data)}'
        else:
            url = f'http://{host}/api/v1/resources/{resource}/{function}'

        try:
            if method.lower() == "get":
                response = requests.get(url)
            elif method.lower() == "post":
                response = requests.post(url, data)
        except requests.ConnectionError as e:
            return "Error"

        if response.status_code == 200:
            return response.json()
        else:
            return None
