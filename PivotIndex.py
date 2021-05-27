class Solution(object):
    def pivotIndex(self, nums):
        totalsum = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (totalsum - leftsum - x):
                return i
            leftsum += x
        return -1
