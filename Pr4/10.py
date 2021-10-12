n=int(input())
k=int(input())
print('Кол-во чисел из ряда Фибоначи: ',n)
print('Порядковый номер числа,начиная с которого вычисляется сумма: ',k)
s1=1
s2=1
a=0
sum=0
for i in range(3,n+1):
    if i<=k:
       a=s1+s2
    sum=s1+s2
    s1=s2
    s2=sum
print('Сумма = ',sum+a)
