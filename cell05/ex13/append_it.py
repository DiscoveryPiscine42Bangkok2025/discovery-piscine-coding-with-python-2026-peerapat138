#!/usr/bin/python3
import sys
if len(sys.argv[1:]) >= 1:
   for i in sys.argv[1:]:
        if "ism" in i:
           print(i)
        else:
           print(i, end=(""))
           print("ism")
else:
    print("none")