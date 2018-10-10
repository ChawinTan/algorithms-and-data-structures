class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        temp, pos = [], []
        
        for i in range(len(S)):
            if S[i].isalpha() == False:
                temp.append(S[i])
            else:
                temp.append(" ")
                
        counter = 0
        for i in range(len(S)-1,-1,-1):
            if S[i].isalpha():
                while temp[counter] != " ":
                    counter += 1
                temp[counter] = S[i]
        
        return "".join(temp)
