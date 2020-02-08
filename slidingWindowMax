import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        else:
            max_arr = []     
            nums = [-i for i in nums]
            for i in range(0,(len(nums)-k+1)):
                sub_list = nums[i:(i+k)]
                heapq.heapify(sub_list)
                max_arr.append(heapq.heappop(sub_list))
            
            max_arr = [-i for i in max_arr]

            return max_arr
