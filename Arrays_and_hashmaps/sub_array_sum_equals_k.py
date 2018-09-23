    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total_sum, dicty = 0, {0: 1}
        res = 0
        for i in range(len(nums)):
            total_sum += nums[i]        #include the sum of the existing number
                                        #next total_sum - k will give answer of nums[i] == k
            if total_sum - k in dicty:       #we can get to K after dicty[total_sum -k] to current point
                res += dicty[total_sum - k]
                     
            if total_sum in dicty:         # number of ways we can get to total sum
                dicty[total_sum] += 1
            
            else:
                dicty[total_sum] = 1
        
        return res
