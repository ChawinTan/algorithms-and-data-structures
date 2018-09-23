class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(num_start, num_end, acc):
            if len(acc) == n*2:
                res.append("".join(acc))
            
            if num_start > num_end:              #everytime num_start is added, it will generate the opposite
                acc.append(")")
                dfs(num_start, num_end+1, acc)
                acc.pop()
            
            if num_start < n:                    
                acc.append("(")
                dfs(num_start+1, num_end, acc)
                acc.pop()
        dfs(0,0,[])
        return res
'''
first iteration goes to 3rd if statement - "("
second iteration goes to 2nd and 3rd if statement - "()" and "(("
... and so on
'''
