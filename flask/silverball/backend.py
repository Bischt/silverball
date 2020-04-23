import requests
import urllib.parse
import json
from flask import Flask, Blueprint, jsonify, request, session, g, redirect, url_for, abort, render_template, flash, \
    current_app


class PlayfieldAPI:

    def __init__(self, host, port):
        self.playfield_api_host = host
        self.playfield_api_port = port

    def api_request(self, method, resource, function, data):

        if method.lower() == "get" and data is not None:
            url = f'http://{self.playfield_api_host}:{self.playfield_api_port}/api' \
                  f'/v1/resources/{resource}/{function}/{urllib.parse.quote(data)}'
        else:
            url = f'http://{self.playfield_api_host}:{self.playfield_api_port}/api' \
                  f'/v1/resources/{resource}/{function}'

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

    def parse_json(self, json_to_parse):
        """
        Take JSON as string returned from a Playfield API request
        and parse data section into list of dicts {field_name=data}
        :param json_to_parse:
        :return: return_data
        """
        json_obj = json.loads(json_to_parse)
        return_data = []
        for row in json_obj['data']:
            row_dict = {}
            for key, value in row.items():
                row_dict[key] = value
            return_data.append(row_dict)
        return return_data
