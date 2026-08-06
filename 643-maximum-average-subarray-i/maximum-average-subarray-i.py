class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxavg=-102010
        left=0
        su=0
        for i in range(len(nums)):
            su+=nums[i]
            if i>=k-1:
                avg=su/k
                maxavg=max(avg,maxavg)
                su-=nums[left]
                left+=1
        return maxavg