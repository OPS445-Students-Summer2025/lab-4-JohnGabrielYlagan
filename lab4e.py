#!/usr/bin/env python3

'''
Lab 4e - Strings search and validate
Author ID: jgylagan
'''
#import 

def is_digits(sobj):
    offset = 0
    # offset starting point of 0
    length = len(sobj) 

    while offset < length:  
        # will loop while offset is less than the length  
        if sobj[offset] not in '0123456789':
    # checks each character in the string if they are number digit or not
            return False  
        #return False if containing non digits
        offset = offset + 1
        # then move to next character in string

    return True               
    # return if the check says all numbers return true
   


    # main block
if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')