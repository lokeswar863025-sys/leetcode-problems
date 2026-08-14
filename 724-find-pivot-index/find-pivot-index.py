class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=[0]
        su=0
        for i in range(len(nums)):
            su+=nums[i]
            a.append(su)
        print(a)
        for j in range(len(nums)):
            if a[j]==a[len(nums)]-a[j+1]:
                return j
        return -1
