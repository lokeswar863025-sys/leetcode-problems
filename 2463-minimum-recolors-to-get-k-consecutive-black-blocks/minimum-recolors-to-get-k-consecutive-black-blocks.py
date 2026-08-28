class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        count=0
        mi=100000
        for right in range(len(blocks)):
            if blocks[right]=='W':
                count+=1
            if right>=k-1:
                mi=min(mi,count)
                if blocks[left]=='W':
                    count-=1
                left+=1
        return mi

            
                
            