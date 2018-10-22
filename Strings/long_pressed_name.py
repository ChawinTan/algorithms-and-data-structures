class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        count = 0
        x = len(name) - 1

        typed = [y for y in typed]
        while True:
            if count > x or len(typed) < len(name):
                break
            elif name[count] != typed[count] and typed[count] == name[count-1]:
                typed.pop(count)
            elif name[count] != typed[count]:
                return False
            elif name[count] == typed[count]:
                count += 1
        
        if len(typed) > len(name):
            return True if "".join(typed[:len(name)]) == name else False
           
        if "".join(typed) == name:
            return True
        else:
            return False
