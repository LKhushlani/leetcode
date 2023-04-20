class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bracketsToRemove = set()
        stack  = []
        
        for i, c in enumerate(s):
            
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                bracketsToRemove.add(i)
            else:
                stack.pop()
        
        bracketsToRemove = bracketsToRemove.union(set(stack))
        stringBuilder = []
        for i,c in enumerate(s):
            if i not in bracketsToRemove:
                stringBuilder.append(c)
        
        return "".join(stringBuilder)


Solution().minRemoveToMakeValid('L(ee)(t(()coe')

