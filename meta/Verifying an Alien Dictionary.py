from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        orderIndex = { c:i for i,c in enumerate(order)}
        print(orderIndex)

        for i in range(len(words)-1):
            w1 , w2 = words[i], words[i+1]
            print(w1, w2)
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if orderIndex[w2[j]] < orderIndex[w1[j]]:
                        print('True')
                        return False
                    break
            print('REs')
        return True





w = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
s = "zkgwaverfimqxbnctdplsjyohu"

Solution().isAlienSorted(w,s)
        