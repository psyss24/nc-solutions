class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        leftMax=0
        rightMax=0
        area=0
        for i in range(len(height)):
            leftMax = max(height[l], leftMax)
            rightMax = max(height[r], rightMax)
            area += min(leftMax, rightMax) - height[i]
            if leftMax<rightMax:
                l+=1
            else:
                r+=-1
        return area