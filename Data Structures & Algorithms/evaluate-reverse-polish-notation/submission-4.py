class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c not in "+/-*":
                stack.append(int(c))
            else:
                val=0
                a=stack.pop()
                b=stack.pop()
                if c=='+':
                    val = b+a
                elif c=='-':
                    val = b-a
                elif c=='*':
                    val = b*a
                elif c=='/':
                    val = int(b/a)
                stack.append(val)
        return stack[-1]
