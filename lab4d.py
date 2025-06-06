#!/usr/bin/env python3

'''
Lab 4d - Strings 1
Author ID: jgylagan
'''

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(stra):
    return stra[0:5]
    # return the first 5 values in the stringa

def last_seven(strb):
    return strb[-7:]
    # return the last 7 values in the stringb

def middle_number(inta):
    return str(inta)[1:3]
    # coverting the inta values to string
 
def first_three_last_three(stringa,stringb):
    return stringa[0:3] + stringb[-3:]
    # combining the first 3 values from stringa with last 3 from stringb


    # main block
if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))