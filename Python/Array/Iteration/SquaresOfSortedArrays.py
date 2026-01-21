class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis = []
        for i in nums:
            lis.append(i*i)
        lis.sort()
        return lis