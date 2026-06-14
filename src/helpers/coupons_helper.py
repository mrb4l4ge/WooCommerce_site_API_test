from apitest_frw.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger

class CouponsHelper(object):

    def __init__(self):
        self.wooAPI_utility = WooAPIUtility()

    def get_coupon_by_id(self, coupon_id):
        return self.wooAPI_utility.get(f'coupons/{coupon_id}')
    
    def call_generate_coupon(self, payload):
        return self.wooAPI_utility.post('coupons', params=payload, expected_status_code=201)
    
