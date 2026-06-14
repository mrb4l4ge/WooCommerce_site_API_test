
from apitest_frw.src.utilities.wooAPIUtility import WooAPIUtility
from apitest_frw.src.dao.orders_dao import OrdersDAO
import os
import json

class OrdersHelper(object):

    def __init__(self):
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))
        self.woo_helper = WooAPIUtility()
        self.orders_dao = OrdersDAO()

    def create_order(self, additional_args=None):
        
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')

        with open(payload_template) as f:
            payload = json.load(f)

        # if user adds more payload, then update it
        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter 'additional_args' must be a dict, but found {type(additional_args)}"
            payload.update(additional_args)

        rs_api = self.woo_helper.post('orders', params=payload, expected_status_code=201)
        return rs_api
    
    def verify_order_is_created(self, order_json, exp_cust_id, exp_products):

        # verify response
        assert order_json, f"Create order response is empty"
        assert order_json['customer_id'] == exp_cust_id, \
            f"Create order with given customer id returned bad customer id. " \
            f"Expected customer id: {exp_cust_id}, but got: {order_json['customer_id']}"
        assert len(order_json['line_items']) == len(exp_products), \
            f"Expected {len(exp_products)} item in order, but got {len(order_json['line_items'])} \n" \
            f"Order id: {order_json['id']} \n"

        # verify db
        order_id = order_json['id']
        line_info = self.orders_dao.order_lines_by_order_id(order_id)

        assert line_info, f"Create order, line info not found in db. Order ID: {order_id}"

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == 1, f"Expected 1 line item, but found {len(line_items)}. Order ID: {order_id}"

        # get list of product id-s in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]
        for product in exp_products:
            assert product['product_id'] in api_product_ids, f"Creqate order does not have at least 1 expected product in db. \n" \
                                                                f"Product id: {product['product_id']}. Order ID: {order_id}"

    def call_update_an_order(self, order_id, payload):
        rs_api = self.woo_helper.put(f'orders/{order_id}', params=payload)
        return rs_api
    
    def call_retrieve_an_order(self, order_id):
        rs_api = self.woo_helper.get(f'orders/{order_id}')
        return rs_api






