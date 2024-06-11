import os
from dotenv import load_dotenv

load_dotenv()

STRAPI_URL = os.environ.get('STRAPI_URL')
STRAPI_AUTHOR = os.environ.get('AUTHOR')
MONGO_HOST = os.environ.get('MONGO_HOST')