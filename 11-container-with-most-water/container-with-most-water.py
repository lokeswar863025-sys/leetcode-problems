class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        area=0
        right=len(height)-1
        a=0
        b=0
        while left<right:
            a=right-left
            h=min(height[left],height[right])
            b=a*h
            area=max(area,b)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area

