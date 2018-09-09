class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(path, nums):
            res.append(path)
            for i in range(len(nums)):
                dfs(path+[nums[i]], nums[i+1:])
                
        dfs([], nums)
        return res
