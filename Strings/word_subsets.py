import collections
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        compare_B = collections.Counter()
        
        for b in B:
            for letter, count in collections.Counter(b).items():     #items return a tuple of the count of items in b
                compare_B[letter] = max(compare_B[letter], count)    #keep only the max count of the letter
        
        res = []
        for a in A:
            count_A = collections.Counter(a)                         
            if all(count_A[c] >= compare_B[c] for c in compare_B):   #check if letters in a is bigger than letters stored in b dictionary
                res.append(a)
        return res
