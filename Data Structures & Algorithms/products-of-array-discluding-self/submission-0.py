class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create products of items before i and create products of items after i
        # then simply multiply products before and after i together
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        output = []
        for i in range(len(nums)):
            output.append(pref[i] * suff[i])

        return output