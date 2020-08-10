# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:09:53 2020

@author: Lycoris radiata
"""
address = "1.1.1.1"
transfer = ''
for index, val in enumerate(address):
     if address[index] == '.':
         transfer += '[.]'
     else:
         transfer += val
print(address)

