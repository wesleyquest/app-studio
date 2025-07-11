import reflex as rx
import os
from dotenv import load_dotenv
#
#
load_dotenv()

config = rx.Config(
    app_name="app_studio",
    #db_url=os.getenv('POSTGRES_DB_URL'),
)

