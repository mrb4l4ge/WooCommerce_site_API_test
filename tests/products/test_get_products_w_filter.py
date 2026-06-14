
import pytest
from datetime import datetime, timedelta

from apitest_frw.src.helpers.products_helper import ProductsHelper
from apitest_frw.src.dao.products_dao import ProductsDAO


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):
         
        # create data
        x_days_from_today = 30
        tmp_date = datetime.now() - timedelta(days=x_days_from_today)
        after_created_date = tmp_date.strftime('%Y-%m-%dT%H:%M:%S')
        # tmp_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        # after_created_date = tmp_date.isoformat()
        payload = dict()
        payload['after'] = after_created_date
        payload['per_page'] = 100
    
        # make API call
        product_helper = ProductsHelper()
        rs_api = product_helper.call_list_products(payload)
        assert rs_api, f"Empty response for 'list products with filter'"


        # get data from db
        products_dao = ProductsDAO()
        db_products = products_dao.get_products_created_after_given_date(after_created_date)

        # verify response match db
        assert len(rs_api) == len(db_products), \
            f"List products with filter 'after' returned unexpected number of products." \
            f"Expected: {len(db_products)}" \
            f"Actual: {len(rs_api)}"
        
        ids_in_api = [i['id'] for i in rs_api]
        ids_in_db = [i['ID'] for i in db_products]

        ids_diff = list(set(ids_in_api) - set(ids_in_db))

        assert not ids_diff, f"Mismatch ids of API filtered products with same filtered from DB" 

        

