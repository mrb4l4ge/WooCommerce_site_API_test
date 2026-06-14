
import pytest
import logging as logger
from apitest_frw.src.utilities.requestUtility import RequestUtility

@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():
    req_helper = RequestUtility()
    rs_api = req_helper.get('customers')
    logger.debug(f"Response of list all: {rs_api}")

    assert rs_api, f"Response of list all customers is empty."

    


