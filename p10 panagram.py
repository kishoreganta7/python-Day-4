#write a python program to print valid panagram or not panagram

import string
s=input()
s=s.lower()
s1=string.ascii_lowercase
if set(s) == set(s1):
    print("panagram")
else:
    print("not a panagram")
