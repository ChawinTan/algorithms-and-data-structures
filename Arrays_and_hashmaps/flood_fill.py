class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        curr_color = image[sr][sc]
        
        if curr_color == newColor:
            return image
        
        else:
            row, width = len(image), len(image[0])
            stack, visited = [[sr, sc]], set()
            
            while stack:
                node = stack.pop()
                
                if str(node) not in visited:
                    visited.add(str(node))
                    image[node[0]][node[1]] = newColor
                    
                    if node[0]-1 >= 0 and image[node[0]-1][node[1]] == curr_color: 
                        stack.append([node[0]-1, node[1]])

                    if node[0]+1 <= row-1 and image[node[0]+1][node[1]] == curr_color: 
                        stack.append([node[0]+1, node[1]])

                    if node[1]-1 >= 0 and image[node[0]][node[1]-1] == curr_color: 
                        stack.append([node[0], node[1]-1])

                    if node[1]+1 <= width-1 and image[node[0]][node[1]+1] == curr_color: 
                        stack.append([node[0], node[1]+1])
                    
            return image
