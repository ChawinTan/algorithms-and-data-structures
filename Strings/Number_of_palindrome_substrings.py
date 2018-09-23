class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        board = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for single in range(len(s)):     # mark all single number as palindrome
            board[single][single] = 1
            
        # static = front pointer
        # moving = back pointer
        
        for static in range(len(s)-1, -1, -1):
            for moving in range(static+1, len(s)):
                if static + 1 == moving:         # determine if the immediate neigbour to the individual can be a palindrome
                    if s[static] == s[moving]:
                        board[static][moving] = 1
                    else:
                        board[static][moving] = 0
                else:
                    if s[static] == s[moving] and board[static + 1][moving - 1] == 1:   # if not neighbor to individual, check if the middle string is a palindrome as computed previously
                        board[static][moving] = 1       # add 1 to static to move pointer in front
                    else:                               # deduct 1 from moving to move pointer back one letter
                        board[static][moving] = 0
        
        return sum([sum(counts) for counts in board])
