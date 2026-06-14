import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    if not domain:
        domain = 'apitest.com'
        if not email_prefix:
            email_prefix = 'testuser'

    email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20
    password = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {
        'email': email,
        'password': password,
    }

    return random_info

def generate_random_string(length=10, prefix=None, suffix=None):

    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string

    if suffix:
        random_string = random_string + suffix
    
    return random_string