# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 15:14:53 2024

@author: Carolina
"""

import os
import mmap

# List to store paths of desired files
res = []

baseDir = os.path.abspath(os.getcwd())

def findKeyWord(path, keyword):
    with open(path, 'rb', 0) as file:
        s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(keyword.encode()) != -1:
            print(f'String exists in the file {path}')

def desiredFile(path, extension):
    global res
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(extension):
                res.append(os.path.join(root, name))

# Starting point for directory walk
desiredFile(baseDir, ".output")

# Searching for the keyword in the collected files
for path in res:
    findKeyWord(path, 'SUCESSO')