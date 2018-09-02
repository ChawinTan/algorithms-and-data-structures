class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far, max_end_here = -10000000000, 0
        
        for i in range(len(nums)):
            max_end_here += nums[i]
            
            if max_so_far < max_end_here:
                max_so_far = max_end_here
            
            if max_end_here < 0:
                max_end_here = 0
                
        return max_so_far

'''
Kadane's algorithm
'''
