class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if(k == len(nums)):
            total = sum(nums)
            return total/k

        curr = 0
        for i in range(k):
            curr += nums[i]
        count = 1
        ans = curr/k
        for i in range(k,len(nums)):
            curr += nums[i]-nums[i-k]
            ans = max(ans,curr/k)
            count +=1
        return ans
        