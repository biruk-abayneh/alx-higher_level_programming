#!/usr/bin/python3
for a in range(0, 10):
    for b in range(1, 10):
        if a == b or a > b:
            continue
        else:
            if (a == 8): print("89")
            else: print(f"{a}{b}", end=", ")
