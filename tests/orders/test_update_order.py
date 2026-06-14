
from apitest_frw.src.helpers.orders_helper import OrdersHelper
from apitest_frw.src.utilities.wooAPIUtility import WooAPIUtility
from apitest_frw.src.utilities.genericUtilities import generate_random_string
import pytest

pytestmark = [
    pytest.mark.regression,
    pytest.mark.orders,
]

@pytest.mark.parametrize("new_status",
                         [
                             pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
                             pytest.param('completed', marks=pytest.mark.tcid56),
                             pytest.param('on-hold', marks=pytest.mark.tcid57),
                         ])
def test_update_order_status(new_status):

    # new_status = 'cancelled'
    
    # create an order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    cur_status = order_json['status']
    assert cur_status != new_status, f"Current status of order is already {new_status}. " \
                                     f"Unable to run test."

    # update the status
    order_id = order_json['id']
    payload = {'status': new_status}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to '{new_status}', " \
                                                    f"but status is still {new_order_info['status']}."


@pytest.mark.tcid58
def test_update_order_status_random_string():
    woo_helper = WooAPIUtility()

    new_status = 'abcdef'

    # create an order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the status
    payload = {'status': new_status}
    rs_api = woo_helper.put(f'orders/{order_id}', params=payload, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', \
        f"Update order status to random string did not have correct code in response. Expected 'rest_invalid_param' " \
            f" Actual: {rs_api['code']}"
    assert rs_api['message'] == 'Invalid parameter(s): status', \
        f"Update order status to random string did not have correct message in response. Expected 'Invalid parameter(s) status' " \
            f" Actual: {rs_api['message']}"

@pytest.mark.tcid59
def test_update_order_customer_note():

    # create an order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the customer note
    rand_string = generate_random_string(40)
    payload = {'customer_note': rand_string}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    assert new_order_info['customer_note'] == rand_string, f"Update order's 'customer_note' field failed. " \
                                                           f"Expected: {rand_string}. Actual: {new_order_info['customer_note']}."