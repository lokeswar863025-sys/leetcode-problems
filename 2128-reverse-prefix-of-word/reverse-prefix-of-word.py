class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=-1
        word=list(word)
        if ch in word:
            a=word.index(ch)
            i=0
            while i<a:
                word[i],word[a]=word[a],word[i]
                i+=1
                a-=1
            return ''.join(word)
        return ''.join(word)