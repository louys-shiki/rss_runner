# -*- coding: utf-8 -*-
# @Author: louys
# @Date:   2017-03-31 15:53:58
# @Last Modified by:   louys
# @Last Modified time: 2017-04-01 18:53:48
import json
import config

fp = open(config.json_file,'r',encoding='utf-8')
content = fp.read()
content = json.loads(content)

num = len(content['children'][0]['children'])

for i in range(num):
    try:
        print(content['children'][0]['children'][i]['children'][0]['title'])
        print(content['children'][0]['children'][i]['children'][1]['title'])
        print(content['children'][0]['children'][i]['children'][2]['title'])
        print('---------------------{}----------------------'.format(str(i)))
    except:
        pass


