class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=[]
        word1=list(word1)
        word2=list(word2)
        for i in range(len(word1)):
            a.append(word1[i])
            for j in range(i,len(word2)):
                a.append(word2[j])
                break
        while j<len(word2)-1:
            j+=1
            a.append(word2[j])
        return ''.join(a)

            

        