''' using staticstics '''
class Solution(object):
    def threeSumMulti(self, A, target):
        c = collections.Counter(A)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) / 6  #binomial for 3
            elif i == j != k: res += c[i] * (c[i] - 1) / 2 * c[k]     #binomial, chose r numbers in nCr ways
            elif k > i and k > j: res += c[i] * c[j] * c[k] #chose each number is n ways
        return res % (10**9 + 7)

''' subsets '''
class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        def dfs(path, nums, target):
            if len(path) == 3 and sum(path) == target:
                res.append(1)
                
            for i in range(len(nums)):
                dfs(path+[nums[i]], nums[i+1:], target)
        dfs([], A, target)
        return sum(res)%(10**9+7)
