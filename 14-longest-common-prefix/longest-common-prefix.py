class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        strs.sort()
        f = strs[0]
        l = strs[-1]
        for i in range(min(len(f),len(l))):
            if f[i] != l[i]:
                return a
            else:
                a = a + f[i]
        return a
