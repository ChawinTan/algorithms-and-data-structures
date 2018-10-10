class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        min_len = 1000000000000000000
        for word in strs:
            min_len = min(min_len, len(word))
            
        res, test_word = "", strs[0]
        
        for i in range(min_len):
            w = test_word[i] 
            if all(word[i] == w for word in strs):
                res += w
            else:
                return res
        return res
