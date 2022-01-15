# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:06:00 2022

@author: fmuror02
"""

def getPrime(nu):
    print('Numbers:')
    print(2)
    num = 3
    nus = int(nu)
    
    while num < nus:
        import isPrime
        a = isPrime.isPrime(num)
        
        digits = len(str(num))
        
        if a == True:
            print(num)
        else:
            print()
        
        num = num + 2
        
        numt = str(num)
        text1 = open("Prime numbers.txt","w")
        text1.write(numt)
        
        digitst = str(digits)
        text2 = open("Number of digits.txt","w")
        text2.write(digitst)
    
    

    
    