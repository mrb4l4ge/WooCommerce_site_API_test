from apitest_frw.src.utilities.genericUtilities import generate_random_string
from apitest_frw.src.helpers.coupons_helper import CouponsHelper

import pytest

pytestmark = [
    pytest.mark.coupons, 
    pytest.mark.smoke, 
    ]

@pytest.mark.parametrize("discount_type",
                          [
                             pytest.param('percent', marks=[pytest.mark.tcid37, pytest.mark.smoke]),
                             pytest.param('fixed_cart', marks=pytest.mark.tcid38),
                             pytest.param('fixed_product', marks=pytest.mark.tcid39),
                             ])
def test_create_coupons(discount_type):

    # generate sample data
    payload = {
        "code": generate_random_string(5),
        "discount_type": discount_type,
        "amount": "10",
        "individual_use": True,
        "exclude_sale_items": True,
        "minimum_amount": "100.00"
    }

    # make the API call
    coupon_helper = CouponsHelper()
    coupon_rs = coupon_helper.call_generate_coupon(payload)
    rs_code = coupon_rs.get('code')
    payload_code = payload.get('code')

    # verify if response is not empty
    assert coupon_rs, f"Create coupon API response is empty. Payload: {payload}"
    assert rs_code==payload_code, \
        f"Create coupon API call has unexpected code." \
        f"Expected: {payload_code}" \
        f"Actual: {rs_code}"

    # verify if coupon is created via API call
    coupon_id = coupon_rs['id']
    api_coupon = coupon_helper.get_coupon_by_id(coupon_id)
    api_coupon_code = api_coupon['code']

    assert api_coupon_code==payload_code, \
        f"Create coupon has an unexpected coupon code when the same item retrieved through API call." \
        f"Expected code: {payload_code}" \
        f"Retrieved code: {api_coupon_code}"

