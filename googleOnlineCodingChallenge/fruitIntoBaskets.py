'''
You have a row of trees. You are given an integer array fruits where fruits[i] is the type of fruits the ith tree produces.

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets. If you cannot, stop.
Move to the next tree to the right of the current tree. If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.

'''

# On time complexity

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        start =0 
        end = 0
        d = {}
        max_val = 0
        while end < len(fruits):
            d[fruits[end]] = end
            if len(d) >=3:
                min_val = min(d.values())
                del d[fruits[min_val]]
                start = min_val +1 

            max_val = max(max_val,end -start +1)
            end += 1
        return max_val


