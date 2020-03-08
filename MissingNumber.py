#bitwise
On O1
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result ^= i^ nums[i]
            
        return result
        



#other 
new_arr = [-1 for i in range(len(nums)+2)]

for i in range(len(nums)):
    new_arr[nums[i]] = nums[i]
    print(new_arr)
print(new_arr)

for i in range(len(new_arr)):
    if new_arr[i] == -1:
        print(i)
        return i
