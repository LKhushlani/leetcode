class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start_index = 0
        end_index = len(s)-1
        while start_index < end_index:
            # print(start_index)
            # print(end_index)
            s[start_index], s[end_index] = s[end_index], s[start_index]
            start_index += 1
            end_index -= 1
