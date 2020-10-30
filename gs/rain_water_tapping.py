class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0
        
        leftmax  , rightmax = [height[0]], [ height[-1]]
        result = 0

        for i in range(1, len(height)):
            leftmax.append(max( leftmax[-1], height[i])) 
            rightmax.append(max(rightmax[-1], height[-i-1]))

        rightmax = rightmax[::-1]

        for i in range(1,len(height)-1):
            water = min(leftmax[i-1], rightmax[i+1]) - height[i]
            if water > 0:
                result += water
            
        return result