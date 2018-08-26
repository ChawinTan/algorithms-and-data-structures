class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack, len_counter, counter, copy = [], 0, 0, head
        
        while head:
            len_counter += 1
            head = head.next
       
        halfway = int(len_counter)/2 +1 if len_counter%2 > 0 else int(len_counter)/2
        
        while copy:
            counter += 1
            
            if counter <= halfway:
                stack.append(copy.val)
            if len_counter%2 > 0 and counter == halfway:
                stack.pop()
            elif counter > halfway and copy.val == stack[len(stack)-1]:
                stack.pop()
            elif counter > halfway and copy.val != stack[len(stack)-1]:
                return False
            
            copy = copy.next
            
        return True if not stack else False
