# Create your views here.
import pymysql
from rest_framework.decorators import api_view

from myapp.handler import APIResponse
from myapp.models import OpLog
from myapp.serializers import OpLogSerializer
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

        cursor = conn.cursor()
        sql = 'select * from b_op_log'
        # 执行sql
        cursor.execute(sql)
        # 查找所有内容
        data = cursor.fetchall()
        print(len(data))
        if len(data) > 100:
            for i in range(0, len(data)-100):
                res = data[i][0]
                sql1 = "delete from b_op_log where id=%s"
                cursor.execute(sql1, res)
            conn.commit()
            conn.close()






        opLogs = OpLog.objects.all().order_by('-re_time')[:100]
        serializer = OpLogSerializer(opLogs, many=True)
        return APIResponse(code=0, msg='查询成功', data=serializer.data)
