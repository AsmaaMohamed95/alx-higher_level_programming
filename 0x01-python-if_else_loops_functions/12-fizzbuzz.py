#!/usr/bin/python3
def fizzbuzz():
    for x in range(0, 101):
        if x % 3 == 0:
            if x % 3 == 0 and x % 5 == 0:
                print("FizzBuzz ", end="")
            else:
                print("Fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(x), end="")
