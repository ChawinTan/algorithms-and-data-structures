class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #linkedlist cycle 2 logic.
        #repeated number will cause the pointer to get stuck in a loop
        slow, fast = nums[0], nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
