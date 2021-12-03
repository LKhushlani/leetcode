# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left = right = 0
        result = 0

        while right < len(s):
            print("left", s[left], 'right', s[right])
            chars[ord(s[right])] +=1
            print(chars[ord(s[right])],ord(s[right]))

            while chars[ord(s[right])] >1:
                print(chars[ord(s[right])], chars[ord(s[right])]>1)
                chars[ord(s[left])] -= 1
                left += 1
                print("In while",s[right], chars[ord(s[right])],ord(s[right]))

            right += 1
            result = max(result, right - left +1)
            print('res', result)
        
        return result

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))










            
