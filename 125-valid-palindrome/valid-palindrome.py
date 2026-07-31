class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        a=""
        for i in s:
            if i.isalnum():
                a=a+i
        i=0
        j=len(a)-1
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
        return True

        



        