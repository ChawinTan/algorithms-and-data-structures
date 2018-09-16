''' when solving questions involving an array
    that contains the height of a wall and we
    have to find the biggest area, use 2 pointers,
    one at the front and one at the back, move the one
    shorter as the only way to get a larger area
    is to find a bigger wall
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1, p2, area, temp_area = 0, len(height) -1, 0, 0 
        
        while p1 != p2:
            if height[p1] < height[p2]:
                temp_area = height[p1]*(p2-p1)
                p1 += 1
            else:
                temp_area = height[p2]*(p2-p1)
                p2 -= 1
            if temp_area > area:
                area = temp_area
        return area
