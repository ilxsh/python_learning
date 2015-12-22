#!/usr/bin/env python3
# -*- coding: utf-8 -*-

while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print('Length is of sufficient lenth.')
print('Done')
