class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_value = prefix = nums[0]
       
        for i in range(1,len(nums)):
            prefix += nums[i]
            min_value = min(min_value,prefix)
        if min_value > 0:
            return 1
        return 1-min_value