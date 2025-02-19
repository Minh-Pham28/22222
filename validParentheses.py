class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            dictin = {')':'(', ']':'[', '}':'{'}

            for char in s:
                if char in dictin:
                    if stack and stack[-1] == dictin[char]:
                        stack.pop()
                    else:
                        return False  
                else:
                    stack.append(char)
            return not stack
    
    ''' stack = []
        closing = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch not in closing:
                stack.append(ch)
            else:
                if stack and stack[-1] == closing[ch]:
                    stack.pop()
                else:
                    return False
'''
                    
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([)]"))      # False
print(sol.isValid("{[]}"))      # True


                    