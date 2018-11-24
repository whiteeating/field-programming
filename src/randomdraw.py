# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:26:42 2018

@author: 14194
"""
import os 
import random
import math 
from txt_solve import select_QQ

def fun_1(a,b):
    return a*b
def fun_2(a,b):
    return a**b
def fun_3(a,b):
    return a*b*b
def fun_4(a,b):
    return  a+b


def draw_winner(value,count):
    bonus = select_QQ(value)
    length = bonus[0]
    #print(length)
    QQ = bonus[1]
    # 随机算法
    #print(count)
    result = []
    while (len(result)<count):
        a = random.randint(2,20)
        b = random.randint(2,20)
        #print("测试")
        #print(a)
        #print(b)
        randnum = random.randint(1,4)
        if randnum == 1:
            mid = (fun_1(a,b))
            if mid >=length:
                mid = mid%length 
            result.append(mid)
        if randnum == 2:
            mid = (fun_2(a,b))
            if mid >=length:
                mid = mid%length
            result.append(mid)
        if randnum == 3:
            mid = (fun_3(a,b))
            if mid >=length:
                mid = mid%length
            result.append(mid)
        if randnum == 4:
            mid = (fun_4(a,b))
            if mid >=length:
                mid = mid%length
            result.append(mid)
        result = set(result)
        result = [p for p in result]
    print(result)     
    # print(result)
    
    global winner
    os.remove('result.txt')
    os.remove('final_result.txt')
    os.remove('QQ_NUM.txt')
    if bonus:
        winner = [QQ[p] for p in result]
    print(len(winner))
    return winner