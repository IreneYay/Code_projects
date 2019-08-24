import math
from collections import defaultdict
class Graph:
    """
    This class represents a directed graph using adjacency list representation
    """
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        # You may put any required initialization code here
        self.edges = defaultdict(list)  # edges
        self.graph = [set() for _ in range(n)]  # adjacency_list
    def insert_edge(self, u, v, w):
        """
        functions takes in two vertices, checks if they exist and adds an edge and weight
        """
        t = (u, v) #tuple of vertices
        if t not in self.edges: #if vertices already exist
            self.size += 1
        if len(self.graph) < u + 1 or len(self.graph) < v + 1: #checks if one vertex is missing
            raise IndexError
        self.graph[u].add(v) #append v to u
        self.graph[v].add(u) #append u to v since graph is undirected
        self.edges[u, v] = w #weight from u to v
        self.edges[v, u] = w #weight from v to u

    def degree(self, v):
        """
        function takes in vertex and returns its degree
        """
        return len(self.graph[v]) #returns the degree of vertices in graph
    def are_connected(self, u, v):
        """
        function checks if two vertices are connected
        """
        if len(self.graph) < u + 1 or len(self.graph) < v + 1: #checks if one or both vertices are in the graph
            raise IndexError #if not raises an IndexError
        return u in self.graph[v] #iterates through vertices in the graph
    def is_path_valid(self, path):
        """
        function checks takes in a path and checks if it is valid
        """
        for i in range(len(path) - 1):#iterates through path
            if not self.are_connected(path[i], path[i + 1]): #calls are_connected
                return False
        return True
    def edge_weight(self, u, v):
        """
        function takes in two vertices and retuns the the weight of that edge
        """
        if len(self.graph) < u + 1 or len(self.graph) < v + 1:
            raise IndexError
        for i in self.graph[u]: #iterates through vertices in the graph
            if i == v: #if two vertices are same
                return self.edges[(u, v)] #return tuple of edges
        return math.inf #if not return infinity
    def path_weight(self, path):
        """
        function takes in a path and finds the total weight of a path (sum of edge weights)
        """
        if not self.is_path_valid(path): #checks if path is valid
            return math.inf
        total_weight = 0
        for i, v in enumerate(path): #enumerate path for indices
            if i == len(path) - 1: #checks to see if index is not out of range
                break
            total_weight += self.edge_weight(path[i + 1], v) #calls edge_weight to find weight and adds to total_weight
        return total_weight
    def does_path_exist(self, u, v):
        """
        function takes in two vertices and checks whether a path exists between those two vertices
        """
        if len(self.graph) < u + 1 or len(self.graph) < v + 1:
            raise IndexError
        path = [False] * (self.order) #creates a list of vertices
        queue = [] #initializes an empty queue
        queue.append(u) #appends u to queue
        path[u] = True #if that path exists
        while queue: #if queue is not empty
            n = queue.pop(0) #pops the first vertex
            if n == v: #if that vertex is equal to v
                return True
            for i in self.graph[n]: #iterates through graph
                if path[i] == 0: #checks for path of that vertex
                    queue.append(i) #appends to queue
                    path[i] = True
        return False
    def find_min_weight_path(self, u, v):
        """
        function takes in two vertices and finds a path of minimum weight between two vertices
        """
        visited = set() #set of visited vertices
        unvisited = [None] *(self.order) #set of unvisited vertices
        distances = {}
        predecessors = {}
        distances[u] = 0

        if len(self.graph) < u + 1 or len(self.graph) < v + 1:
            raise IndexError
        if u == v:
            return [u]
        if not self.does_path_exist(u, v):
            raise IndexError
        #DIJKSTRA ALGORITHM
        while unvisited:
            #find minimum distance from the unvisited nodes
            min_node = None
            for node in unvisited:
                if min_node is None:
                    min_node = node
                elif distances[node] < distances[min_node]:
                    min_node = node
            if min_node is None:
                break
            unvisited.remove(min_node)
            visited.add(min_node)
            #distance = distances[min_node]
            neighbors = self.graph[min_node]
            for neighbor in neighbors:
                if neighbor in unvisited:
                    new_distance = distances[min_node] + neighbors[neighbor]
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = min_node
        curr_vertex = v
        path = []
        while curr_vertex != u:
            path.append(curr_vertex)
            curr_vertex = predecessors[curr_vertex]
        path.append(u)
        return path
    def is_bipartite(self):
        """
        Determines if the graph is bipartite using depth_first_search function
        """
        group = {} #empty dictionary
        def dfs(a, b): #depth_first_search function takes in two arguments
            if a in group: #
                return b == group[a]
            group[a] = b
            return all(dfs(y, 1 - b) for y in self.graph[a])
        return all(dfs(a, 0) for a in range(len(self.graph)) if a not in group)
        
