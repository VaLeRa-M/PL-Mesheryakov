n=int(input())
s1=1
s2=1
sum=0
for i in range(3,n+1):
    sum=s1+s2
    s1=s2
    s2=sum
print(sum)
