class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in range(len(s)):
            if s[i] != '*':
                a.append(s[i])
            else:
                a.pop()
        return ''.join(a)
