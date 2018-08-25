#backtracking to print(and store)
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        :where start = start index, end = end index of the array
        '''
        
        def backtrack(num, start, end):

            if start == end:
                print(num)
                '''res.append(num[::]) to store result in array'''
                
            for i in range(start, end+1):
                num[start], num[i] = num[i], num[start]
                backtrack(num, start+1, end)
                num[start], num[i] = num[i], num[start]
        
        
        backtrack(nums, 0, len(nums)-1, [])

#dfs an array to create a path to append
'''
:To dfs an array in parralel, remove one element from the array in a loop recursively
:eg: dfs([1,2,3],[]) => dfs([2,3], [1])
                     => dfs([1,3], [3]) etc...
'''
res = []

def permute(nums, path):
    if not nums:
        res.append(path)

    for i in range(len(nums)):
        permute(nums[:i]+nums[i+1:], path[i])
permute([1,2,3], [])
        
