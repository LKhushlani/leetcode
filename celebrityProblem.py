# def knows(a,b):
#     return true or false 

def check_celebrity(int n):
    
    candidate = 0 
    for i in range(1,n):
        if knows(candidate, i):
            candidate = i

    for i in range(0,n):
        if candidate != i and (knows(candidate,i) or !knows(i,candidate)):
            return -1

    return candidate
            
