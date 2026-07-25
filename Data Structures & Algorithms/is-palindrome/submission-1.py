class Solution:
    def isPalindrome(self, s: str) -> bool:
        # iterate throuhg array, copy lowcase char to seperate string
        # return equality check on new str and its reversal

        forward = []
        for c in s:
            if c.isalnum():
                forward.append(c.lower())
        n=len(forward)  

        return forward == forward[::-1]
                