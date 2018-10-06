class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            carry = a&b   #and operator to carry the matching ones 
            a = a^b       #get opposing pairs of ones and add them, considered done when partner value is 0
            b = carry<<1  #shift the 2 matching ones left since adding them is multiplying by 2
        return a          #carry will be zero once all bits are shifted appropriately
