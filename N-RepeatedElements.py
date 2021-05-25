class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for j in xrange(1, 4):
            for i in xrange(len(nums)-j):
                if nums[i]==nums[i+j]:
                    return nums[i]
