class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # maintain 2 pointers
        l=0
        r= len(nums)-1
        n=0
        while l <= r:
            mid = (l+r) //2
            cur= nums[mid]
            if cur == target:
                return mid
            elif cur > target:
                r=mid-1
            elif cur < target:
                l=mid+1
        return -1