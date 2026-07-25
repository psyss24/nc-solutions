class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        d = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for c in s:
            if c in d.values():
                stack.append(c)
            else:
                # if its a closing bracket, it must be the most recent one we added
                if not stack or d[c] != stack[-1]:
                    return False
                # safely remove from stack
                stack.pop()
            # stack should be empty at the end
        return len(stack) == 0