class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        shifts = 0
        for i in range(l):
            if arr[i] == 0:
                shifts += 1 

        for i in range((l-1), -1, -1):
            if shifts+i <l:
                arr[shifts +i] = arr[i]
            if arr[i] == 0:
                shifts -=1
                if shifts +i < l:
                    arr[shifts+i] = 0
