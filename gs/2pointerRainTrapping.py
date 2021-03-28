class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0
        
        result = 0
        leftmax,rightmax = 0,0
        left , right = 0, len(height)-1 

        while left < right:

            if height[left] <= height[right]:
                leftmax = max(leftmax, height[left])
                result += leftmax - height[left]
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                result += rightmax - height[right]
                right -=1


        return result
        