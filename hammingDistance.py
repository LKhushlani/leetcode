class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        result = bin(x ^ y)
        for i in range(2,len(result)):
            if result[i] == '1':
                count += 1

        return count
