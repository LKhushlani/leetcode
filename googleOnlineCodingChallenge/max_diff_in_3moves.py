def minDifference(self, A):
    A.sort()
    return min(b - a for a, b in zip(A[:4], A[-4:]))



class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4: return 0
        nums.sort()
        return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])




