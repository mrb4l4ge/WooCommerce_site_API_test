
from apitest_frw.src.utilities.requestUtility import RequestUtility
from apitest_frw.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger

class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()
        self.wooAPI_utility = WooAPIUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f'products/{product_id}')
    
    def call_generate_product(self, payload):
        return self.requests_utility.post('products', payload=payload, expected_status_code=201)
    
    def call_update_product(self, product_id, payload):
        return self.wooAPI_utility.put(f'products/{product_id}', params=payload)
    
    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # add the current page number to the call
            payload['page'] = i

            rs_api = self.requests_utility.get(f'products', payload=payload)

            # if there is no response stop the loop cause there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products