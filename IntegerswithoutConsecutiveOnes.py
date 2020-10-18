class Solution:
    def findIntegers(self, num):
        zeroes = [0 for i in range(num)]
        ones =  [0 for i in range(num)]
        ones[0] = zeroes[0] = 1
        
       
        for i in range(1,num):
            zeroes[i] = zeroes[i-1]+ ones[i-1]
            ones[i] = zeroes[i-1]
            

        return zeroes[num-1]+ ones[num-1]


o = Solution()
print(o.findIntegers(5))

0 00 10 | 000 100 010 | 
1 01    | 001 101     |

0    0         - 1
1    1          - 1
2    10         - 1 
3    11         -0
4    100        - 1
5    101        - 1

