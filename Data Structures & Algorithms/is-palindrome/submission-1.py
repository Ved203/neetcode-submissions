# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         clean = ""
#         for c in s:
#             if c.isalnum():
#                 clean += c.lower()
#         return clean == clean[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()

        flag = True
        left = 0
        right= len(clean)-1

        while (left< right):
            if clean[left]!=clean[right]:
                flag = False
                break
            left +=1
            right -=1
            
        return flag
















