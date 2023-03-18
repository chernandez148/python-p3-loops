#!/usr/bin/env python3
def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    
    print("Happy New Year!")

def square_integers(int_list):
    squared_list = []

    for squared in int_list:
        num_squared = squared * squared
        squared_list.append(num_squared)
    return squared_list

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)
