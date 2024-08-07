#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:51:52 2024

@author: rohitha_matwada
"""

# reading whole file contents --- this won't work for alrge files bc the program can crash
file_content = " "

with open('anna_karenina.txt') as file:
    file_content = file.read()

print(file_content)

# reading a file line by line

with open('anna_karrenina.txt') as file:
    while True:
        line = file.readline()
        
        if not line:
            break
        
        print(line)
    
