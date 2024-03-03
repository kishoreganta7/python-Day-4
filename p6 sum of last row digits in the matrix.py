#write a python program to print sum of elements in last row

r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    sum+=i[c-1]
print(sum)
