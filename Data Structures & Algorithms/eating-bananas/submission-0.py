class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # run binary search on the space of possible answers
        # for each middle candidate sol:
            # compute hours, check if its valid, update parameters if so
        l=1
        r=max(piles)
        while l<=r:
            middle = (l+r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/middle)
            if hours <= h:
                ans = middle
                r=middle-1
            else:
                l=middle+1
        return ans 