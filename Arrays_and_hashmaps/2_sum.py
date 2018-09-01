class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        
        for i in range (len(nums)):
            if target - nums[i] not in store:
                store[nums[i]] = i

            elif target-nums[i] in store:
                return [store[target-nums[i]], i]
