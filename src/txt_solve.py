    # -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:15:55 2018

@author: 14194
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:54:13 2018

@author: 14194
"""
import sys
import re
import numpy as np
import pandas as pd
from datetime import datetime
match2 = '2'

"""def matchh(value):
    match2=value
    return match2 """
def wipe_empty():
    file = open('record.txt','r',encoding='utf-8')
    fnew = open('result.txt','w',encoding='utf-8')
    lines = file.readlines()
    l = [x for x in lines]
    match1 = '系统消息'
    for n in range(len(l)):
        data = l[n].strip()
        if len(data)!= 0:
            data = data+'\n'
            if match1 not in l[n]:
                fnew.write(l[n])
            else:
                l[n] = l[n+1] = ''
                fnew.write(l[n])
                fnew.write(l[n+1])
                
def select_1(value):
    wipe_empty()
    fnew = open('result.txt','r+',encoding='utf-8')

    filenew = open('final_result.txt','w',encoding='utf-8')
    f = fnew.readlines()
    
    # print(f)
    l = [x for x in f]
    match2 = value
    
    print(match2+'ok1')
    
    for n in range(len(l)):
        if match2 in l[n]:
            filenew.write(l[n-1])
            l[n] = match2+'\n'
            filenew.write(l[n])
def select_QQ(value):
    select_1(value)
    f = open('final_result.txt','r',encoding='utf-8')
    qqNum = open('QQ_NUM.txt','w')
    person = []
    able_person = []
    s = set([])
    b = 1
    for line in f.readlines():
        rule = re.compile(r'[1-9][0-9]{5,9}')
        r = re.compile(r'[1-9](0){6,10}')
        m1 = r.search(line)
        if m1:
            b = m1.group()
            b = int(b)
        m = rule.search(line)
        if m:
            a  = m.group()
            a = int(a)
            #print(m.group())
            person.append(a)
        s = set(person)
    #print(s)
    for x in s:
        if x!= b:
            able_person.append(x)
            x = str(x)
            qqNum.write(x+'\n')
    return len(able_person),able_person

    
    
    
           
    
           
    
