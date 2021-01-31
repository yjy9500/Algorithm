r,g,b=map(int,input().split())

def solution(r,g,b):
    sum=0
    for i in range(0,r):
        for j in range(0,g):
            for k in range(0,b):
                print("%d %d %d" %(i,j,k))
                sum=sum+1

    print(sum)

solution(r,g,b)
                
    
