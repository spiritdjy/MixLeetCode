class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '[{(':
                stack.append(i)
            elif i in ']})':
                if not stack:
                    return False
                if i == ']' and stack[-1] != '[':
                    return False
                if i == '}' and stack[-1] != '{':
                    return False
                if i == ')' and stack[-1] != '(':
                    return False
                stack = stack[:-1]
        if stack:
            return False
        return True
