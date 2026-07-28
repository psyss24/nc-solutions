class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                # Left half is sorted
                if nums[l] <= target < nums[mid]:
                    # is target inside of left half?
                        # if it is discard right half
                    r = mid - 1
                else:
                    # if it isnt can discard left half
                    l = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


