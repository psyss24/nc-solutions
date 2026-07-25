class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sort = sorted(nums)
        result = []
        for i in range(n):
            # 
            if i > 0 and sort[i] == sort[i - 1]:
                continue
            # repeatedly compute 2 sum from i -> n
            l=i+1
            r=n-1

            target = 0 - sort[i]
                # compute 2 sum
            while l<r:
                val = sort[l] + sort[r]
                if val < target:
                    l+=1
                elif val > target:
                    r+=-1
                elif val == target:
                    result.append([sort[i],sort[l],sort[r]])
                    l+=1
                    r+=-1
                    # when searching for new triplets within this level, dont reuse the same left and right pointers
                    while l < r and sort[l] == sort[l - 1]:
                        l += 1
                    # 
                    while l < r and sort[r] == sort[r + 1]:
                        r -= 1
        return result
