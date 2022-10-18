a = [1,2,3,4,5,67,78,89]

def delete(x,y):
    x = x[:y]+x[y+1:]
    return x
    
print(delete(a,2))

