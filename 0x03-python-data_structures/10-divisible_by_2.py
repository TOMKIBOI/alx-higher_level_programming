#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    quotient = []
    for num in my_list:
        quotient.append(num % 2 == 0)
    return quotient
