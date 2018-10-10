''' maximum subarray sum of circular array '''
'''
totalsum - min_sum
'''
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        total_sum, max_end_here, max_so_far, min_end_here, min_so_far = 0, 0, -10000000000000000, 0, 1000000000000000
        
        for i in range(len(A)):
            total_sum += A[i]
            
            #max sub array
            max_end_here += A[i]
            max_so_far = max(max_so_far, max_end_here)
            if max_end_here < 0:
                max_end_here = 0
                
            #min sub array
            min_end_here += A[i]
            min_so_far = min(min_so_far, min_end_here)
            if min_end_here > 0:
                min_end_here = 0
                
        #if max_so_far is smaller than 0, it means total_sum = min_so_far as all the other elements are smaller than 0
        return max(max_so_far, total_sum-min_so_far) if max_so_far > 0 else max_so_far
