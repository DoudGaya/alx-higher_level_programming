#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0 or idx > len(my_list)):
        return None
    for i in range(len(my_list)):
        if (i == idx):
            print('Element at the index {} is {}'.format(idx, my_list[i]))
            break
            return
