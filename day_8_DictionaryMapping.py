"""Objective
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure."""


N = int(input())
d = dict{}

for i in range(0, N):
    name, number = input().split()
    d[name] = number

for i in range(0, N):
    name = input()
    if name in d:
        print("{}={}".format(name, d[name]))
    else:
        print("Not found")
        
        
n=int(input().strip())
phone_book={}
for i in range(n):
    x= input().strip()
    listx = list(x.split(' '))
    phone_book[listx[0]] = listx[1]
name=[]
try:
    while True:
        inp = input().strip()
        if inp != "":
            name.append(inp)
        else:
            break
except EOFError:
    pass
for i in name:
    c=0
    if i in phone_book:
 
        print(i+'='+phone_book[i])
 
    else:
        print('Not found')