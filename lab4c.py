#!/usr/bin/env python3

'''
Lab 4c - Dictionaries
Author ID: jgylagan
'''

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']


def create_dictionary(keys, values):
    seneca_dictionary = {} 
    # empty dictionary for keys and values
    dictionary_length = 0 
    # starting point of 0 for length
    while dictionary_length < len(keys) and dictionary_length < len(values): 
        # loop will repeat uwhile the length is less than keys and values
        seneca_dictionary[keys[dictionary_length]] = values[dictionary_length]
        dictionary_length = dictionary_length + 1
        # plus 1 move the index 
        
    return seneca_dictionary
    # return the final result of the dictionary



def shared_values(dict1, dict2):
    return(set(dict1.values()).intersection(set(dict2.values()))) 
# return sets containing only common values from each dictionary


# main block
if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)