class Solution:
    def maxFrequencyElements(self, n: List[int]) -> int:
        a=defaultdict(int)
        m=0
        for i in n:
            a[i]+=1
            m=max(m,a[i])
        c=0
        for i in a:
            if a[i]==m:
                c+=a[i]
        return c