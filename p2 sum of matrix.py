#write a python program to print sum of given matrix

r,c=int(input("Rows:")),int(input("columns:"))
l=[]

for i in range(r):
    l.append(list(map(int,input().split())))

sumn=0
for i in l:
    print(i)
    sumn+=sum(i)
print(sumn)
