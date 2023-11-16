#Write a program to reverse every kth row in a matrix 
r=int(input())
c=int(input())
m=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    m.append(a)
for i in range(r):
    for j in range(c):
        print(m[i][j],end=" ")
    print()
print("The original list is : " + str(m))
K=int(input('Enter the row value want to reverse: '))
 
res = []
for idx, ele in enumerate(m):
    if (idx + 1) % K == 0:
        res.append(list(reversed(ele)))
    else:
        res.append(ele)
print("After reversing every Kth row: " + str(res))
