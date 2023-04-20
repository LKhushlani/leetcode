'''
https://leetcode.com/problemset/all/?page=1&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&companySlugs=facebook
'''
'''
Input: nums = [2,3,-2,4]
Output: 6
'''

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        min_so_far = nums[0]
        max_so_far  = nums[0]
        result = max_so_far

        for i in range(1,len(nums)):
            num = nums[i]
            print(num)
            temp_max = max(num, max_so_far*num, min_so_far * num)
            print('tmax', temp_max)
            min_so_far  = min(num, min_so_far*num, max_so_far*num)
            print('minS', min_so_far)
            max_so_far = temp_max 
            print('max_s', max_so_far)
            result = max(max_so_far, result)
            print(result)
            
Solution().maxProduct([2,-5,-2,-4,3])


