
from apitest_frw.src.utilities.genericUtilities import generate_random_string
from apitest_frw.src.helpers.products_helper import ProductsHelper
from apitest_frw.src.dao.products_dao import ProductsDAO
import pytest

pytestmark = [
    pytest.mark.products, 
    pytest.mark.smoke, 
    ]

@pytest.mark.tcid26
def test_create_1_simple_product():

    # generate sample data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10.99"

    # make the API call
    product_helper = ProductsHelper()
    product_rs = product_helper.call_generate_product(payload)
    rs_name = product_rs.get('name')
    payload_name = payload.get('name')

    # verify if response is not empty
    assert product_rs, f"Create product API response is empty. Payload: {payload}"
    assert rs_name==payload_name, \
        f"Create product API call has unexpected name." \
        f"Expected: {payload_name}" \
        f"Actual: {rs_name}"

    # verify if product in db
    product_dao = ProductsDAO()

    product_id = product_rs['id']
    db_product = product_dao.get_product_by_id(product_id)
    db_name = db_product[0]['post_title']

    assert db_name==payload_name, \
        f"Create product API call has mismatched name with name of same item in the DB." \
        f"API call name: {payload_name}" \
        f"DB name: {db_name}"


