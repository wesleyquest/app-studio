import os
import psycopg2
from dotenv import load_dotenv
#
#
load_dotenv()

ygtest_conn = psycopg2.connect(
        database=os.getenv('ygtest_db'), #'ygtest',
        user=os.getenv('ygtest_user'), #'wesleyquest',
        password=os.getenv('ygtest_password'), #'Wqasdf01!',
        host=os.getenv('ygtest_host'), #'211.218.17.10',
        port=os.getenv('ygtest_port'), #'5432'
)

