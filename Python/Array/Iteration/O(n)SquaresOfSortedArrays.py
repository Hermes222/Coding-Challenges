class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) -1
        squared = [0]*len(nums)
        print(squared)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[right]) > abs(nums[left]):
                squared[i]=nums[right]*nums[right]
                right -= 1
            else:
                squared[i]=nums[left]*nums[left]
                left += 1
        return squared