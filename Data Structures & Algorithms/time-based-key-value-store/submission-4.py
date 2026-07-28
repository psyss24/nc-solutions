class TimeMap:

    def __init__(self):
        self.store = {}



    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        l=0
        r=len(self.store[key])-1
        val=""
        while l<= r:
            
            mid=(l+r)//2
            if self.store[key][mid][0] > timestamp:
                # sol invalid, discard right half
                r= mid-1
            else:
                # sol valid but maybe we can find better one
                val = self.store[key][mid][1]
                l=mid+1
        return val


