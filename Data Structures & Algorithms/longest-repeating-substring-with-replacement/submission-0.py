class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        maxFreq = 0
        maxLen = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            # window size - max freq refers to diff characters
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen

            # compute max freq, validity
            # validity is, k >= count of max char - window size
                # valid -> expand window
                # not valid -> shrink