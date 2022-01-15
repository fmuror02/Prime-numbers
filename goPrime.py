# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 20:15:13 2022

@author: fmuror02
"""

import getPrime
print('Hello. Welcome to the python code that generates infinite prime numbers. You can read how this works in our text file in the package "Setup.txt".')
print('If you have, to start just introduce the highest number you want the code to generate (infinte numbers can shut down the program). ')
nu = input('Highest number you want the code to generate (no spaces):')
getPrime.getPrime(nu)
