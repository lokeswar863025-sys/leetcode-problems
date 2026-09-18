class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        b=[]
        for i in s:
            if i != '#':
                a.append(i)
            else:
                if not a:
                    continue
                else:
                    a.pop()
        for j in t:
            if j != '#':
                b.append(j)
            else:
                if not b:
                    continue
                else:
                    b.pop()
        if ''.join(a) == ''.join(b):
            return bool(1)
        else:
            return bool(0)