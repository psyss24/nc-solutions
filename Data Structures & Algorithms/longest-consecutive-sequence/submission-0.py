class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start of seq is a number s.t. num -1 doesnt exist
        # iterate through array if number is a starter then start counting the seq
        # chec if starter + 1 exists, if so increment k if not go to next num in array
        numbers = set(nums)
        k=0
        for n in nums:
            if n-1 not in numbers:
                m=n
                length=1
                while m+1 in numbers:
                    m+=1
                    length+=1
                    if m not in numbers:
                        break
                k=max(k,length)
        return k