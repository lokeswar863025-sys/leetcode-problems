class Solution:
    def minimizedStringLength(self, s: str) -> int:
        a=set(list(s))
        return len(a)