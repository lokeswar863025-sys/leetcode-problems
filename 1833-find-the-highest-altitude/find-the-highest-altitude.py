class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        su=0
        b=[]
        for i in gain:
            su+=i
            b.append(su)
        mx=0
        for j in b:
            mx=max(mx,j)
        return mx