# write m python program to print find maximum and minimum value i matrix using tuple and sum of maximum and minimum value


r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(tuple(map(int,input().split())))


min,max=1000,0
print(tuple(l))
for i in l:
    print(i)
    for j in i:
        if j>max:
            max=j
        if j<min:
            min=j
print("minimum value",min)
print("maximum value",max)
print(min+max)



