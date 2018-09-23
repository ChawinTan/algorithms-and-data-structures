class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res, acc = [], {}
        
        for word in strs:
            if "".join(sorted(word)) not in acc:
                acc["".join(sorted(word))] = [word]
            else:
                acc["".join(sorted(word))].append(word)
        for key in acc:
            res.append(acc[key])
        return res
