# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:00:19 2020

@author: Lycoris radiata
"""

a = 123
#a = -123
#a = 210


A = ['']
aa = str(a)
front = len(aa)-1
flag = 0

for i in range(front, -1, -1):
    if aa[i] != '0' and aa[i] != '-':
        A[0] = A[0]+aa[i]
    if aa[i] == '-':
        flag = 1

if flag == 0:
    ans = int(A[0])
    print(ans)

else:
    ans = -(int(A[0]))
    print(ans)
