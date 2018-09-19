class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        ''' initialize graph_dict to empty dict if no graph is provided'''
        self.__graph_dict = graph_dict 

        ''' return vertices '''
    def vertices(self):
        return list(self.__graph_dict.keys())

        ''' return edges '''
    def edges(self):
        return self.__generate_edges()

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
    def __generate_edges(self):
        res = []
        for vertex in self.__graph_dict:
            for neighbor in vertex:
                res.append((vertex, neighbor))
        return res

        ''' find shortest path '''
    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
            
        if start_vertex not in graph:
            return None

        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path
        return None

        ''' find all path between start and end '''
    def find_all_path(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return [path]

        if start_vertex not in graph:
            return []

        paths = []
        for vertex in graph[start_vertex]:
            print(paths)
            print(vertex)
            if vertex not in path:
                extended_paths = self.find_all_path(vertex, end_vertex, path)

                for p in extended_paths:
                    paths.append(p)
                
        return paths

g = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }

graph = Graph(g)

graph.find_all_path("a", "b")
