
import logging as logger
import os
import pymysql
from apitest_frw.src.utilities.credentialsUtility import CredentialsUtility
from apitest_frw.src.configs.host_configs import DB_HOSTS

class DBUtility(object):

    def __init__(self):
        self.creds_helper = CredentialsUtility()
        self.creds = self.creds_helper.get_db_credentials()

        self.machine = os.environ.get('MACHINE')
        assert self.machine, f"Environment variable 'MACHINE' must be set."

        self.wp_host = os.environ.get('WP_HOST')
        assert self.wp_host, f"Environment variable 'WP_HOST' must be set."

        if self.machine == 'docker' and self.wp_host == 'local':
            raise Exception(f"Can not run test in docker if WP_HOST == 'local'")
        
        self.env = os.environ.get('ENV', 'test')


        self.host =  DB_HOSTS[self.machine][self.env]['host']
        self.database =  DB_HOSTS[self.machine][self.env]['database']
        self.table_prefix =  DB_HOSTS[self.machine][self.env]['table_prefix']
        self.port =  DB_HOSTS[self.machine][self.env]['port']

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'], password=self.creds['db_password'], port=self.port)

        return connection
    
    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            logger.debug(f"Executing {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n  Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
         pass
    

