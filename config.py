# Copyright (c) 2021 Itz-fork

import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID",'25252648'))
    API_HASH = os.environ.get("API_HASH",'17a1e3c7f59dd46196f0570f9df34955')
    BOT_TOKEN = os.environ.get("BOT_TOKEN",'7199477809:AAHP3l7vMe_U2LiwQNc657mzqLo4f5re-f0')
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL",'-1002032506013'))
    MONGODB_URL = os.environ.get("MONGODB_URL",'mongodb+srv://alienufowala:kxzen@cluster0.ahif6tl.mongodb.net/')
    BOT_OWNER = int(os.environ.get("BOT_OWNER",'6986912824'))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/IDNCoderXRoot"
    TG_MAX_SIZE = 2040108421
