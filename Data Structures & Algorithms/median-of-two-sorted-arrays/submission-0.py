class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median has half of numbers to left (are smaller), has half to right (are larger)
        # draw line through A and one through B s.t.:
            # left side has half the numbers
            # left side smaller than right
        # binary search over possible partition values

        # binary search smaller array (fewer partitions)
        A, B = nums1, nums2
        if len(B) < len(A):
            B, A = nums1, nums2
        total = len(B) + len(A)
        half = total//2

        l=0
        r=len(A)-1

        while True:
            i = (l+r) // 2
            # compute B partition
            j = half - i - 2
            # set  values around partition
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")
            # only need to compare boundary values
            if Aleft > Bright:
                # left side of a is too big, move a partition leftwards
                r=i-1
            elif Bleft > Aright:
                # left side of b too big, move a partition rightwards
                l=i+1
    # perf partition
            else:
                # odd number of elements
                if total % 2:
                    return min(Aright, Bright)
                # even number of elements
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2