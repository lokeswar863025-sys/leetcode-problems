class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        s=list(s)
        for i in s:
            if i in d.keys():
                d[i]+=1
                a=i
                return a
            else:
                d[i]=1

