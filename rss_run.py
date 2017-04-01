# -*- coding: utf-8 -*-
# @Author: louys
# @Date:   2017-03-31 14:37:33
# @Last Modified by:   louys
# @Last Modified time: 2017-04-01 18:37:27
import requests
import hashlib
import json
import config
from threading import Thread
import re
title = []
uri = []
compare = {}
num = 0
thread_num = config.thread_num
href = []


#返回列表长度，方便后续来跑
def load_json(filename):
    fp = open(filename,'r',encoding='utf-8')
    content = json.loads(fp.read())
    fp.close()
    lt = content['children'][0]['children'][7]['children'] #maybe change
    for i in range(len(lt)):
        title.append(str(lt[i]['title']))
        uri.append(str(lt[i]['uri']))
    return len(lt)

def post(url):
    content = requests.get(url,timeout=10).content
    tmp = content.decode('utf-8')
    content = re.sub(r"\d+", "d+", tmp)
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def single_thread(start,end):
    for i in range(start,end):
        try:
            url = uri[i]
            #print(url)
            md5 = post(url)
            compare[str(i)] = md5
        except Exception as e:
            pass
            #print(url)
            #print(e)

def save():
    num = load_json(config.json_file)
    group_num = int(num/thread_num)
    threads = []
    for i in range(0,thread_num):
        t = Thread(target=single_thread,args=(i*group_num,i*group_num+group_num))
        threads.append(t)
    t = Thread(target=single_thread,args=(thread_num*group_num,num))
    threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()

    print(compare)
    out = open('compare.txt','w',encoding='utf-8')
    out.write(str(json.dumps(compare)))
    out.close()



def deal():
    load = open('compare.txt','r')
    tmp = json.loads(load.read())
    load.close()
    #print(len(tmp),len(compare))
    for i in compare:
        try:
            if tmp[i] == compare[i]:
                pass
            else:
                if uri[int(i)].find('github.com') > 0:
                    pass
                else:
                    print(uri[int(i)],title[int(i)])
                    result = "<a href='%s'>%s</a>" %(uri[int(i)],title[int(i)])
                    href.append(result)
        except Exception as e:
            pass
    out = open('out.html','w')
    for j in href:
        out.write(j)
        out.write('<br>')
    out.close()
    out = open('compare.txt','w')
    out.write(str(json.dumps(compare)))
    out.close()


def main():
    num = load_json(config.json_file)
    group_num = int(num/thread_num)
    threads = []
    for i in range(0,thread_num):
        t = Thread(target=single_thread,args=(i*group_num,i*group_num+group_num))
        threads.append(t)
    t = Thread(target=single_thread,args=(thread_num*group_num,num))
    threads.append(t)
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    deal()


if __name__ == '__main__':
    #save()
    main()
