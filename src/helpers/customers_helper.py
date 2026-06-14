
from apitest_frw.src.utilities.genericUtilities import generate_random_email_and_password 
from apitest_frw.src.utilities.requestUtility import RequestUtility


class CustomerHelper(object):

    def __init__(self):
        self.requests_utility = RequestUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()
            email = ep['email']
        if not password:
            password = 'Password1'

        payload = {}
        payload['email'] = email
        payload['password'] = password 
        payload.update(kwargs)

        create_user_json = self.requests_utility.post('customers', payload=payload, expected_status_code=201)

        return create_user_json