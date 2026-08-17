class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        for b in s:
            if b == '[':
                stack.append(']')
            elif b == '{':
                stack.append('}')
            elif b == '(':
                stack.append(')')

            else:
                if not stack or stack.pop() != b:
                    return False

        return len(stack)==0