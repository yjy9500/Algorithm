a=input()
def fun1(a):
    n=len(a)
    for i in range(0,n):
        num=ord(a[i])+2
        k=chr(num)
        print(k,end='')
def fun2(a):
    n=len(a)
    for i in range(0,n):
        num1=ord(a[i])*7
        num2=num1%80+48
        j=chr(num2)
        print(j,end='')
   
fun1(a)
print('')
fun2(a)
