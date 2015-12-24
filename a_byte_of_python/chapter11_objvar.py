#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Filename: objvar.py

class Person:
    '''Represents a person'''
    population = 0
    def __init__(self, name):
        '''Initializes the person's date'''
        self.name = name
        print('(initializes %s)'%self.name)

        # When this person is crated, he/sehe
        # adds to the population
        Person.population += 1
    def __def__(self):
        '''I am dyding'''
        print('%a says byte'%self.name)
        Person.population -= 1

        if Person.population == 0:
            print('I am the last one.')
        else:
            print("There are still %d people left."%Person.population)

    def sayHi(self):
        '''Greeting by the person'''
            Really, that's all it done'''
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
           print("I am the entry person here.")
        else:
           print('We have %d persons hre.)


    swaroop = Person('swaroop')
    swaroop.sayHi()
    swatroop.howMany()

    kala = Persion('abdule Ralam'):
    kalam.sayHi()
    kalam.howMany()

    swaroop,sayhi()
    swaroop.howMany()
                
