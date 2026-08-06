class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        su=0
        left=0
        count=0
        mx=-10021
        for i in range(len(arr)):
            su+=arr[i]
            if i>=k-1:
                avg=su/k
                su-=arr[left]
                left+=1
                if avg>=threshold:
                    count+=1
        return count