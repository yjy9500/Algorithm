n,m=map(int,input().split())
def solution(n,m):
    b=[]
    c=[]
    for i in range(1,int(n**0.5)+1):
        if(n%i==0):
            b.append(i)
            if(i!=(n//i)):
                b.append((n//i))
        else:
            continue
    for j in range(1,int(m**0.5)+1):
        if(m%j==0):
            c.append(j)
            if(j!=(m//j)):
                c.append((m//j))
    setb=set(b)
    setc=set(c)
    k=list((setb.difference(setc)))
    q=[]
    q=(k+c)
    q.sort()
    return print(" ".join(repr(e) for e in q))
            
solution(n,m)
    