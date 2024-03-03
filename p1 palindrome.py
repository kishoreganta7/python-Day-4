# write python program to print sum of  even palindrome and list if palinedrome in given ragnge

'''s=input()
rev=s[::-1]
if s==rev:
    print("palindrome")
else:
    print("not palindrome")'''


def palindrome(n):
    s=str(n)
    if s==s[::-1]:
        return 1
    else:
        return 0

n,m=int(input()),int(input())
l1,l2=[],[]
for i in range(n,m+1):
    flag =palindrome(i)
    if flag==1:
        l1.append(i)
    if i%2==0:
        if flag==1:
            l2.append(i)
print(l1)
print(sum(l2))

