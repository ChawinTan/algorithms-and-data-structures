#simple recursive solution
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def recursive(n, k, path, index):
            if len(path) == k:
                res.append(path)
                return
            
            for i in range(index, n+1):
                recursive(n, k, path+[i], i+1)
        
        recursive(n, k, [], 1)
        
        return res

#backtracking
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(n, start, k, path, res):
            if k == 0:
                ''' !!!! --- if we use append in recursion, we must make a new copy to append to res!!! '''
                res.append(path[::]) #copies the newly formed path
                return
            
            for i in range(start, n-k+2): #add 2 to iterate up till the max possible number
                path.append(i)
                backtrack(n, i+1, k-1, path, res) #as we deduct 1 from k, range will approach n+1
                path.pop()
                
        backtrack(n, 1, k, [], res)
        
        return res
