class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
        a = []
        for i in arr:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for j in d.values():
            a.append(j)
        return len(a) == len(set(a))