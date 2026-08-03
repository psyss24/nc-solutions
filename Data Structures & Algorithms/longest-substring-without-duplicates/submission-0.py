class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        seen = set()
        maxx = 0
        while r<len(s):
            # go forward until we find dupl
            # keep set of seen?
            # if we see dupl, shrink until its not in seen
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxx = max(maxx, r-l+1)
            r+=1
        return maxx
