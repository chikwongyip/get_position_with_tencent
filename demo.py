"""
@Description : 单独调用演示
@File        : demo.py
@Project     : txmap
@Time        : 2020/4/4 17:37
@Author      : Dexter
@Software    : PyCharm
"""
import os
from pprint import pprint

import requests as req
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv('KEY')

ret = req.get(
    url='https://apis.map.qq.com/ws/geocoder/v1/',
    params={
        'region': '安阳市',
        'address': '红旗渠',
        'key': KEY
    }
).json()

pprint(ret)
