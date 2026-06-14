
import requests
from apitest_frw.src.configs.host_configs import API_HOSTS
from apitest_frw.src.utilities.credentialsUtility import CredentialsUtility
import os
import json
from requests_oauthlib import OAuth1
import logging as logger

class RequestUtility(object):

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]
        self.auth = OAuth1(wc_creds['wc_key'], wc_creds['wc_secret'])

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
        f"Wrong status code. Expected status code is {self.expected_status_code}, but got {self.status_code}." \
        f"URL: {self.url}" \
        f"Response JSON: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json"}
        self.url = self.base_url + endpoint
        data = json.dumps(payload)

        rs_api = requests.post(url=self.url, data=data, headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")
        return self.rs_json


    def get(self, endpoint, payload=None, headers=None, expected_status_code=200):

        if not headers:
            headers = {"Content-type": "application/json"}
        self.url = self.base_url + endpoint
        data = json.dumps(payload)

        rs_api = requests.get(url=self.url, data=data, headers=headers, auth=self.auth)
        
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")
        return self.rs_json