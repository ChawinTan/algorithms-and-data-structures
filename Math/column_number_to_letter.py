''' convert 10-ary digit to 26-ary digit system '''
def convertToTitle(self, n):
    r = ''
    while(n>0):
        n -= 1
        r = chr(n%26+65) + r
        n /= 26
    return r

''' my long winded answer '''
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
    
        reference={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
        
        if n <= 26:
            return reference[n]
        
        elif n <= 52:
            return reference[1]+reference[n-26]
        
        counter, res, remember = 0, "", n
        while n > 26:
            if counter == 0:
                if n%26 == 0:
                    res += 'Z'
                    n-=26
                    counter += 1
                else:
                    res += reference[n%26]
                    n -= n%26
                    counter += 1
            else:
                temp_n, temp_counter = n, counter
                while counter > 0:
                    temp_n = int(temp_n/26)
                    counter -= 1
                if temp_n%26 > 0:
                    res += reference[temp_n%26]
                    n -= (temp_n%26)*26**temp_counter
                else:
                    res += reference[26]
                    n -= 26**(temp_counter+1)
                counter = temp_counter+1
        
        return "".join(list(reversed(res)))
