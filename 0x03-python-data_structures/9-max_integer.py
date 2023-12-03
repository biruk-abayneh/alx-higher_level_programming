#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        if my_list[0] > my_list[1]:
            b = my_list[0]
        elif my_list[0] < my_list[1]:
            b = my_list[1]
        else:
            b = my_list[0]
        for i in my_list:
            if b > i:
                continue
            elif b < i:
                b = i
            else:
                continue
        return b
