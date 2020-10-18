def countStrings(n): 
  
    zeroes=[0 for i in range(n)] 
    ones=[0 for i in range(n)] 
    zeroes[0] = ones[0] = 1
    for i in range(1,n): 
        zeroes[i] = zeroes[i-1] + ones[i-1] 
        ones[i] = zeroes[i-1] 
      
    return zeroes[n-1] + ones[n-1] 
  
# Driver program to test 
# above functions 
  

print(countStrings(3)) 
