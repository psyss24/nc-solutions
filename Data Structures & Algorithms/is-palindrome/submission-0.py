class Solution:
    def isPalindrome(self, s: str) -> bool:
        # iterate throuhg array, copy lowcase char to seperate string
        # return equality check on new str and its reversal

        forward = []
        backward = []
        for c in s:
            if c.isalnum():
                forward.append(c.lower())
        n=len(forward)  
        for i in range (n-1, -1, -1):
            backward.append(forward[i])
        return backward == forward
                