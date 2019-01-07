# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:50:16 2018

@author: Casper
"""
#def gcd(a,b):
#    if a>=b:
#      temp=b
#    else:
#      temp=a  
#    while True:
#        
#        if a>=b:
#            if a % temp ==0 and b % temp==0:
#                return temp
#            else:
#                if temp>1:
#                 temp-=1
#        else: 
#            if b % temp ==0 and a % temp==0:
#                return temp
#            else:
#             temp-=1
#                
#                
#print(gcd(9,12))                
#            
def gcdRecur(a,b):
    
    if b==0:
         return a
    
    return gcdRecur(b,a%b)
    
    
    
print(gcdRecur(253,77))