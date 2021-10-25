class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max =  0
        right_max = 0
        
        left_idx = 0
        right_idx = len(height) -1
        water = 0
        
        while left_idx <= right_idx:
            if height[left_idx] < height[right_idx]:
                left_max = max(height[left_idx], left_max)
                water += left_max - height[left_idx]
                left_idx += 1

            else:
                right_max = max(height[right_idx],right_max)
                water += right_max - height[right_idx]
                right_idx -= 1
                
                
        return water