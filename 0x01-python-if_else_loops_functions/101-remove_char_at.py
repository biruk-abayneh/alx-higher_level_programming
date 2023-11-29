#!/usr/bin/python3
def remove_char_at(str, n):
    str_new = ""
    count = 0
    for i in str:
        count = count + 1
        if (count - 1) != n:
            str_new = str_new + i
        else:
            continue
    return str_new
