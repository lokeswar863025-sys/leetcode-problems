class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        ma=0
        for i in nums:
            if i==1:
                count+=1
                ma=max(ma,count)
            else:
                count=0
        return ma
