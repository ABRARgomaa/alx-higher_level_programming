#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = my_list.copy()
    for i in range(len(a)):
        if (a[i] == search):
            a[i] = replace
    return (a)
