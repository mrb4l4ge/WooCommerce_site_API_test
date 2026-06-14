
from apitest_frw.src.helpers.products_helper import ProductsHelper
from apitest_frw.src.utilities.wooAPIUtility import WooAPIUtility
from apitest_frw.src.utilities.genericUtilities import generate_random_string
import pytest

pytestmark = [
    pytest.mark.regression,
    pytest.mark.products,
]

@pytest.mark.tcid61
def test_update_product_regular_price():
    woo_helper = WooAPIUtility()
    product_helper = ProductsHelper()

    new_regular_price = "16.99"

    # create a product
    payload = {
        'name': generate_random_string(20),
        'type': "simple",
        'price': "10.99" ,
        'regular_price': "10.99" 
    }
    product_rs = product_helper.call_generate_product(payload)
    product_id = product_rs['id']

    # update the regular price
    upd_payload = {
        'regular_price': new_regular_price
    }
    # rs_api = woo_helper.put(f'products/{product_id}', params=upd_payload, expected_status_code=200)
    rs_api = product_helper.call_update_product(product_id, upd_payload)

    # verify response
    assert rs_api['price'] == new_regular_price, \
        f"Update regular price did not give proper response with updated price" \
        f"Product id: {product_id}, Expected price: {new_regular_price}, Actual price: {rs_api['price']}"
    
    # get the product info
    rs_call_api = product_helper.get_product_by_id(product_id)
    import pdb; pdb.set_trace()
    # verify price
    assert rs_call_api['price'] == new_regular_price, \
        f"Update regular price did not give proper updated price when getting product info through api call" \
        f"Product id: {product_id}, Expected price: {new_regular_price}, Actual price: {rs_call_api['price']}"

@pytest.mark.tcid63
def test_update_product_sale_price_changes_on_sale_status():
    product_helper = ProductsHelper()

    new_sale_price = "10.99"

    # create a product
    payload = {
        'name': generate_random_string(20),
        'type': "simple",
        'price': "9.99" ,
        'regular_price': "9.99", 
        'sale_price': "0"
    }
    product_rs = product_helper.call_generate_product(payload)
    product_id = product_rs['id']

    # Verify current on_sale status
    assert product_rs['on_sale'] == False, \
        f"Unexpected 'on_sale' status being 'False' for a newly created product with 'sale_price = 0'. " \
        f"Unable to test on_sale status. Product id: {product_id}"

    # update the regular price
    upd_payload = {
        'sale_price': new_sale_price
    }
    rs_api = product_helper.call_update_product(product_id, upd_payload)

    # verify response
    assert rs_api['on_sale'] == True, \
        f"Update sale price did not give proper response for 'on_sale' status" \
        f"Product id: {product_id}, Expected 'on_sale' status: True, Actual 'on_sale' status: {rs_api['on_sale']}"
    
    # get the product info
    rs_call_api = product_helper.get_product_by_id(product_id)
    # verify price
    assert rs_call_api['on_sale'] == True, \
        f"Update sale price did not give proper updated 'on_sale' status when getting product info through api call" \
        f"Product id: {product_id}, 'on_sale' status: True, Actual 'on_sale' status: {rs_call_api['on_sale']}"

