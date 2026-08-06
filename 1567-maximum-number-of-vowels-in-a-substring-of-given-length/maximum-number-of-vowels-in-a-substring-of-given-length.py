class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx=-1051
        count=0
        left=0
        s=list(s)
        for i in range(len(s)):
            if s[i] in (['a','e','i','o','u']):
                count+=1
            if i>=k-1:
                mx=max(mx,count)
                if s[left] in (['a','e','i','o','u']):
                    count-=1
                left+=1
        return mx
            
