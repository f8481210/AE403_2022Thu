# -*- coding: utf-8 -*-
"""
Created on Fri May  6 18:35:33 2022

@author: N
"""
import heapq

list1 = [4,1,3,2]

heapq.heapify(list1)

print(list1)

#新增 add heapq.heappush(存的list,value)
heapq.heappush(list1,5)
print(list1)

#取出 delete heapq.heappop(list)
heapq.heappop(list1)
print(list1)
