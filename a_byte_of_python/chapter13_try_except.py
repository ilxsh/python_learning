#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Filename: try_except.py

import sys
try:
    s = input('Enter something --> ')
except EOFError:
    print('\nWhy did you do an EOF on me?')
except:
    print('\nSome error / exception occurred.')
    # here, we are not exiting the program

print('Done')
