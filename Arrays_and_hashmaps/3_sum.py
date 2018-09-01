class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, res = len(nums), []
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]: #avoid duplicate solution for the same 2 sum
                continue
            target = nums[i]*-1
            s, e = i+1, N-1
            
            while s<e:    #2 sum loop
                if nums[s] + nums[e] == target:
                    res.append([nums[i], nums[s], nums[e]])
                    s += 1
                    
                    while s<e and nums[s] == nums[s-1]:        #check if the new s is the same to avoid duplicate
                        s += 1
                        
                elif nums[s]+nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return res
                
