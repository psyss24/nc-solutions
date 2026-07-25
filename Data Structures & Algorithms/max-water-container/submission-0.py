class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer
        # per iteration, compute area = l-r * min(heightl,hr)
        # update area if its bigger
        # increment smaller pointer
        l=0
        r=len(heights)-1
        area=0
        while l<r:
            left = heights[l]
            right = heights[r]
            val = (r-l)*(min(left, right))
            if val>area:
                area=val
            if left>right:
                r+=-1
            else:
                l+=1
        return area