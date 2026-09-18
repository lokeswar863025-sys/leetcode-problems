class Solution:
    def minOperations(self, logs: list[str]) -> int:
        a=[]
        for i in logs:
            if i == "../":
                if not a:
                    continue
                else:
                    a.pop()
            elif i == "./":
                continue
            else:
                a.append(i)
        return len(a)