#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func():
    global x
    print('x is',x)
    x = 2
    print('Change local x to',x)
x = 50
func()
print('Value of x is',x)
