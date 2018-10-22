lass Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        temp1, temp2 = [], []
        
        for i in A:
            if i%2 == 0:
                temp1.append(i)
            else:
                temp2.append(i)
                
        res = []
        
        for i in range(len(temp1)):
            res.append(temp1[i])
            res.append(temp2[i])
        return res
