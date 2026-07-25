class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
# brute force
    # for each value
    # see how far we can go left and right without bumping into a smaller value
    # for col[3] which equals 6 if we can go 3 left and 1 right without bumping into smaller value
    # then do 6 x (3+1) = area
    # append this area to stack. repeat for all 

# stack
#  same idea but maintain stack that has working list
#  of bars waiting to bump into a smaller value
#  if n smaller than stack head, it has found smaller value
#   thus compute area and add to area list 
#       it may resolve many previous items so use while not if
# if n larger, then it too needs to wait in stack to be resolved by future value
        stack=[]
        max_area =0

        # create artificial shorter bar 0 incase nothing smaller ever arrives (stack heights wont be resolved)
        for i, height in enumerate(heights + [0]):
            start = i
            while stack and height < stack[-1][1]:
                index, h = stack.pop()
                width = i - index
                max_area = max(max_area, h *width)  
                start = index
            stack.append([start,height])
        return max_area




