class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        if nums is []:
            return 0
        else:
            for i in nums:
                result ^= i
            
        return result
