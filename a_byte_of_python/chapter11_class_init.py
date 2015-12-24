#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print("Hello, my name is", self.name)

p = Person('Swaroop')
p.sayHi()

# This shor example can also be written as Persion('Swaroop').sayHi()
