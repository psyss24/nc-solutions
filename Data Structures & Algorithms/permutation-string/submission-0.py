class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        windowCount = [0] * 26
        w = len(s1)
        # count s1
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for i in range(len(s2)):
            # add current character
            windowCount[ord(s2[i]) - ord('a')] += 1
            # remove character outside window
            if i >= w:
                windowCount[ord(s2[i-w]) - ord('a')] -= 1
            # compare window
            if count1 == windowCount:
                return True
        return False
        