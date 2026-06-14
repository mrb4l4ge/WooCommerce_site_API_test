
from apitest_frw.src.configs.host_configs import WOO_API_HOSTS
from apitest_frw.src.utilities.credentialsUtility import CredentialsUtility
from woocommerce import API
import os
import logging as logger

class WooAPIUtility(object):
    
    def __init__(self):
    
        wc_creds = CredentialsUtility.get_wc_api_keys()
        
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]
        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version='wc/v3',
        )

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
        f"Wrong status code. Expected status code is {self.expected_status_code}, but got {self.status_code}.\n" \
        f"Endoint: {self.endpoint} \n" \
        f"Response JSON: {self.rs_json}"

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.post(wc_endpoint, data=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")

        return self.rs_json

    def get(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.get(wc_endpoint, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json
    
    def put(self, wc_endpoint, params=None, expected_status_code=200):
        rs_api = self.wcapi.put(wc_endpoint, data=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.endpoint = wc_endpoint
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json

if __name__ == '__main__':

    obj = WooAPIUtility()
    rs_api = obj.get('products')
    print(rs_api)
    import pdb; pdb.set_trace()



