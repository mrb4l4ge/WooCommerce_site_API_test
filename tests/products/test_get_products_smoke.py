import pytest
import logging as logger
from apitest_frw.src.utilities.requestUtility import RequestUtility
from apitest_frw.src.dao.products_dao import ProductsDAO
from apitest_frw.src.helpers.products_helper import ProductsHelper

pytestmark = [
    pytest.mark.products, 
    pytest.mark.smoke, 
    ]

@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestUtility()
    rs_api = req_helper.get('products')
    logger.debug(f"Response of list all: {rs_api}")

    assert rs_api, f"Response of list all products is empty."


@pytest.mark.tcid25
def test_get_product_by_id():

    # get product from db
    product_dao=ProductsDAO()

    random_product = product_dao.get_random_product_from_db(1)
    random_product_id = random_product[0]['ID']
    db_name = random_product[0]['post_title']

    # call the API
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(random_product_id)
    api_name = rs_api['name']

    # verify response
    assert db_name == api_name, \
        f"Get product by id returned wrong product. Id: {random_product_id}" \
        f"DB product name: {db_name}" \
        f"API product name: {api_name}"
    


