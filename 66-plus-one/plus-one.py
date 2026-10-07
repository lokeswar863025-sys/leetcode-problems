class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = ''.join(map(str,digits))
        b = int(a) + 1
        c = []
        for i in str(b):
            c.append(int(i))
        return c