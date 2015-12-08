#!/usr/bin/env python3
# -*- utf-8 -*-

def my_pow(x):
    return x * x

print("This is my pow of %d\n"%my_pow(3))

def my_power(x,n=2):
    sum=1
    while n>0:
        sum=sum*x
        n=n-1
    return sum

print("The my_power is %d"%my_power(2))
print("The my_power is %d"%my_power(2,3))

#default non-contant parameter
def add1(L=[]):
    L.append("END")
    return L

print("%s"%add1())
print("%s"%add1())
print("%s"%add1())

#default contant parameter
def add2(L=None):
    if L is None:
        L=[]
    L.append("END")
    return L

print("%s"%add2())
print("%s"%add2())
print("%s"%add2())

#define multi-input parameter using list
def mp_calc1(numbers):
    sum=0
    for i in numbers:
        sum=sum+i*i
    return sum

print("%s"%mp_calc1([1,3,5]))
print("%s"%mp_calc1([1,5,9]))

#define multi-input parameter using tuple
def mp_calc2(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i*i
    return sum

print("%s"%mp_calc2(1,3,5))
print("%s"%mp_calc2(1,5,9))
