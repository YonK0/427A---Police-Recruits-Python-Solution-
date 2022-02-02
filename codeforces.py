
a = int(input())
result = 0 
out = 0 


b = list(map(int, input().split()))
    
for i in b : 
    result += i
    if ( result < 0 ) : 
        out +=1 
        result = 0 
print (out)