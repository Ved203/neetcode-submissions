# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         count=0
#         for i in range(len(s)):
#             seen = set()
#             for j in range(i,len(s)):
#                 if s[j] in seen:
#                     break
#                 seen.add(s[j])
                
#                 count= max(count, j-i+1)
#         return count

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        count=0
        left =0 

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])

            count= max(count, right - left +1)

        return count