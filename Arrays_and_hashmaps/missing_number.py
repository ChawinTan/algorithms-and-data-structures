#hashmap
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dicty = {}
        for i in nums:
            dicty[i] = True
        for j in range(l+1):
            if j not in dicty:
                return j

#sum of 2 numbers
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = (0 + len(nums)) * (len(nums) + 1)/2 #the sum supposed to be
        sum2 = sum(nums)                           # real sum
        return sum1 - sum2
