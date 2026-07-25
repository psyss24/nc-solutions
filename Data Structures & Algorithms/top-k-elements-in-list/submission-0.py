class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create frequency dictionary
        # get list(dictionary.items())

        s = {};
        for n in nums:
            if n in s:
                s[n] +=1
            else:
                s[n] = 1

        nlist = list(s.items())
        top_k = nlist[:k]

    # iterate through list and maintain running top k total
        (index, smallest) = self.smallest_k(top_k)
        for i in range(k, len(nlist)):
            num, freq = nlist[i]
            if freq > smallest:
                top_k[index] = (num, freq)
                # index = num
                index, smallest = self.smallest_k(top_k)

    # iterate through topk and get k nums
        f =[]
        for num, freq in top_k:
            f.append(num)
        return f


    def smallest_k(self, num: List[int]):
        smallest = 1000
        i=0
        for n,f in num:
            if f < smallest:
                smallest = f
                index = i
            i+=1
        return (index,smallest)
            
