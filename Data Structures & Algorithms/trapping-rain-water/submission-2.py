class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftMax=0
        rightMax=0
        area=0
        while l<r:
            leftMax = max(height[l], leftMax)
            rightMax = max(height[r], rightMax)

            if leftMax<rightMax:
                area+=(leftMax-height[l])
                l+=1
            else:
                area+=(rightMax-height[r])
                r+=-1
        return area