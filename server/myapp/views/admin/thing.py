from datetime import datetime

import psutil
from rest_framework.decorators import api_view, authentication_classes
from tabulate import tabulate

from myapp.handler import APIResponse
import pymysql
from myapp.netdata import  NetworkTrafficMonitor
@api_view(['GET'])
def list_api(request):

    if request.method == 'GET':
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="111111",
            db="mysql",
            charset="gbk",

        )
        db = conn.cursor()

        # sql语句
        sql = 'select * from b_netdata'
        # 执行sql
        a = db.execute(sql)
        # 查找所有内容
        data = db.fetchall()
        return APIResponse(code=0, msg='查询成功', data=data)





