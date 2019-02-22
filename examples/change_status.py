# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth
from qiniu import BucketManager

# 需要填写你的 Access Key 和 Secret Key
access_key = ''
secret_key = ''

q = Auth(access_key, secret_key)

bucket = BucketManager(q)

# 空间名
bucket_name = 'bucket_name'

# 文件名
key = 'file_name'

# 条件匹配，只有匹配上才会执行修改操作
# cond可以填空，一个或多个
cond = {"fsize": "186371",
        "putTime": "14899798962573916",
        "hash": "FiRxWzeeD6ofGTpwTZub5Fx1ozvi",
        "mime": "image/png"}

ret, info = bucket.change_status(bucket_name, key, '0', cond)
print(info)
