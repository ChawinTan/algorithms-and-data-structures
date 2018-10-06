class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs([], s, res)
        return res
    
    def dfs(self, path, s, res):
        if not s:
            res.append(path)
            return 
        for i in range(1, len(s)+1):
            if self.is_pal(s[:i]):
                self.dfs(path+[s[:i]], s[i:], res)
            
    def is_pal(self, s):
        return s == s[::-1]
