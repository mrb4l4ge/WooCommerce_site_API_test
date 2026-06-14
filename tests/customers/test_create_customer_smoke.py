import pytest
import logging as logger
from apitest_frw.src.utilities.genericUtilities import generate_random_email_and_password
from apitest_frw.src.helpers.customers_helper import CustomerHelper
from apitest_frw.src.dao.customer_dao import CustomerDAO
from apitest_frw.src.utilities.requestUtility import RequestUtility

@pytest.mark.customers
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    logger.info("TEST: Create new customer with email and password only.")
    
    # create random email and password
    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj =  CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer API returned with the wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer API returned with value for first name, but is should be empty."

    # verify customer is created in database
    cust_dao = CustomerDAO()

    cust_db_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_db_info[0]['ID']
    assert id_in_api == id_in_db, f"Create customer response 'id' is not the same as response 'ID' in db." \
                                    f"Email: {email}"

@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_for_existing_email():

    # get existing email from db
    cust_dao = CustomerDAO()
    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    # call the api
    req_helper = RequestUtility()

    payload = {'email': existing_email, 'password': 'Password1'}
    cust_api_info = req_helper.post(endpoint='customers', payload=payload, expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', \
        f"Create customer with existing user." \
        f"Error code is not correct, expected 'registration-error-email-exists', got {cust_api_info['code']}"

