# Create your views here.
import datetime
import locale
import platform
import random
import time
from multiprocessing import cpu_count

import psutil
from rest_framework.decorators import api_view, authentication_classes
from myapp.handler import APIResponse
from myapp.auth.authentication import AdminTokenAuthtication

@api_view(['GET'])
@authentication_classes([AdminTokenAuthtication])
def Info(request):
    if request.method == 'GET':
        pf = platform.platform()
        processor = platform.processor()
        osName = platform.system()
        memory = psutil.virtual_memory()
        use_percent_C=psutil.disk_usage(psutil.disk_partitions()[0][0]).percent
        use_percent_D=psutil.disk_usage(psutil.disk_partitions()[1][0]).percent
        start_time=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d,%H:%M:%S")
        data = {
            'osName': osName,
            'pf': pf,
            'cpuCount': cpu_count(),
            'processor': processor,


            'memory': round((float(memory.total) / 1024 / 1024 / 1024), 2),
            'usedMemory': round((float(memory.used) / 1024 / 1024 / 1024), 2),
            'percentMemory': round((float(memory.used) / float(memory.total) * 100), 2),
            'start_time':start_time,
            'use_percent_C': use_percent_C,
            'use_percent_D': use_percent_D,

        }

        return APIResponse(code=0, msg='查询成功', data=data)
