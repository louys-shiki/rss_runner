# -*- coding: utf-8 -*-
# @Author: louys
# @Date:   2017-03-31 15:53:58
# @Last Modified by:   louys
# @Last Modified time: 2017-03-31 16:41:19
import json

fp = open('bookmarks.json','r',encoding='utf-8')
out = open('out.txt','w',encoding='utf-8')
content = fp.read()
content = json.loads(content)

lt = content['children'][0]['children'][7]['children']

for i in range(len(lt)):
    print(lt[i]['title'],lt[i]['uri'])
    out.write(str(lt[i]['title'])+'\r\n')
    out.write(str(lt[i]['uri'])+'\r\n')

out.close()