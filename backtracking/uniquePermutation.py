#simple backtracking
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(nums, start, end):
            if start == end and nums not in res:
                res.append(nums[::])
                
            for i in range(start, end+1):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(nums, start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(nums, 0, len(nums)-1)
        return res

#dfs(more effecient)
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
