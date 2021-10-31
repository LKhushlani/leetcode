# [-2,1,-3,4,-1,2,1,-5,4]
# [4,-1,2,1] 
'''
cs = -2 + 1 = -1 
mx = -2 , -1 = -1 
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = -float("inf")
        currentSum = 0
        for num in nums:
            currentSum += num
            if num > currentSum:
                currentSum = num
            maxSum = max(maxSum,currentSum)

        return maxSum

s = Solution()
maxSum = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(maxSum)

            