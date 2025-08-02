#!/usr/bin/env python3

import sys

def divisions(x,y):
    x=int(x)
    y=int(y)
    if y == 0:
        return "The second number can't be 0"
    else:
        return x/y


print(divisions(sys.argv[1],sys.argv[2]))
#This fuction divide two arguments that the users typed on shell