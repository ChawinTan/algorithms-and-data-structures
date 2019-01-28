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


''' backtracking '''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(path, nums, i):
            res.append(path[::])
            
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path, nums[i+1:], i)
                path.pop()

        backtrack([], nums, 0)
        return res
