# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import re
import sys
from time import sleep
from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main()  -> None:
        region_id     = 'cn-shanghai'
        access_key    = 'LTAI5t89ZhkMmZYgeHjFL5ei'
        secret_key    = 'YtcskxxcACDmU1qshwqdoOSYo2sisJ'
        instance_name = 'mytest*'
        index_regex   = '.*-([0-9]+)$'
        page_number   = 1
        page_size     = 5
        

        client = Sample.create_client(access_key, secret_key)

        while True:
           #  构建请求参数
           request_parameter= ecs_20140526_models.DescribeInstancesRequest(
               region_id=region_id,
               instance_name=instance_name,
               page_number=page_number,
               page_size=page_size
           )

           # 调用请求
           response = client.describe_instances(request_parameter)
           # 获取主机列表数组
           instances = response.to_map()['body']['Instances']['Instance']
           #print("主机数量: {}.".format(len(instances)))
           if len(instances) == 0:
               break

           for instance in instances:
               hostname      = instance['InstanceName']
               hostPrivateIp = instance['NetworkInterfaces']['NetworkInterface'][0]['PrimaryIpAddress']
               ret = re.search(index_regex, hostname)
               if ret:
                   gameId = ret.group(1)
               print("{} ansible_ssh_host={} GameId={}".format(hostname, 
                         hostPrivateIp,
                         gameId)
                    )
           page_number += 1 
           #sleep(3)

         
if __name__ == '__main__':
    Sample.main()
