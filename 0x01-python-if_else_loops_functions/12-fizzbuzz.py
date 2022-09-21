#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print('{}{}'.format(FIZZ, BUZZ), end=" ")
        elif i % 3 == 0:
            print('{}'.format(FIZZ), end=" ")
        elif i % 5 == 0:
            print('{}'.format(BUZZ), end=" ")
        else: 
            print(i)
