#!/usr/bin/env python3

'''
Lab 4b - Comparing lists
Author ID: jgylagan
'''

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    return list(set(l1).union(set(l2)))
    # return the union of list 1 and list 2

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    return list(set(l1).intersection(set(l2)))
    # return matching values from both lists

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    return list(set(l1).symmetric_difference(set(l2)))
    # return the diff of list 1 and 2

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))

