class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict ''' initialize graph_dict to empty dict if no graph is provided'''

        ''' return vertices '''
        def vertices(self):
            return list(self.__graph_dict.keys())

        ''' return edges '''
        def edges(self):
            return __self.generate_edges()

        ''' add vertex '''
        def add_vertex(self, vertex):
            if vertex not in self.__graph_dict:
                self.__graph_dict[vertex] = []

        ''' add edge '''
        '''
           assumes that edge is of type set, tuple or list
           as there can be multiple edges between 2 vertices
        '''
        def add_edge(self, edge):
            edge = set(edge)
            (vertex1,vertex2) = tuple(edge)

            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].append(vertex2)
            else:
                self.__graph_dict[vertex1] = [vertex2]

        ''' generate edges '''
        def __self.generate_edge(self):
            res = []
            for vertex in self.__graph_dict:
                for neighbor in vertex:
                    res.append((vertex, neighbor))
            return res
