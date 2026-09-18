class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        for i in range(len(s)):
            if s[i] not in a:
                a.append(s[i])
            else:
                if s[i] == a[-1]:
                    a.pop()
                else:
                    a.append(s[i])
        return ''.join(a)