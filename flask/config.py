import os

from dotenv import load_dotenv
load_dotenv(verbose=True)

class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")