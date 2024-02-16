from typing import Generic, TypeVar
from edge import Edge

V = TypeVar('V')  # Generic type for a vertex


class Graph(Generic[V]):
    """
    Graph class represents an undirected graph with generic vertices and
    edges connecting vertices. Vertices are stored in a list for easy
    lookup via their index. Each vertex has a list of edges it is connected to,
    i.e. an adjacancy list.
    """

    def __init__(self, vertices=None):
        """
        Initialize the graph with the given vertices.
        """
        if vertices is None:
            vertices = []
        self.vertices = vertices
        self.edges = [[] for _ in vertices]

    @property
    def vertices_count(self):
        return len(self.vertices)

    @property
    def edges_count(self):
        return sum(map(len, self.edges))

    def add_vertex(self, vertex: V):
        """ 
        Add a vertex to the graph.

        Args:
            vertex (V): Vertex to be inserted to the graph.

        Returns:
            The index of the vertex added.
        """
        self.vertices.append(vertex)
        self.edges.append([])
        return self.vertices_count - 1

    def add_edge(self, edge: Edge):
        """
        Add an edge to connect two vertices.

        Args:
          Instance of the Edge class.
        """
        self.edges[edge.from_u].append(edge)
        self.edges[edge.to_v].append(edge.reversed_edge())

    def add_edge_by_indices(self, u, v):
        """
        Use vertex indices to create an instance of the Edge class
        and add the edge to the graph.
        """
        edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, vertex1, vertex2):
        """
        Add an edge between the two given vertices by looking
        up the indices.
        """
        u = self.vertices.index(vertex1)
        v = self.vertices.index(vertex2)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index):
        """
        Returns:
          The vertex at the given index.
        """
        return self.vertices[index]

    def index_of(self, vertex):
        """
        Returns:
          The index of the given vertex.
        """
        return self.vertices.index(vertex)

    def neighbors_for_index(self, index):
        """
        Returns:
          A list of neighboring vertices for the vertex at the given index.
        """
        return list(map(self.vertex_at, [e.to_v for e in self.edges[index]]))

    def neighbors_for_vertex(self, vertex):
        """
        Locate the index of the given vertex. This function passes index
        to the helper function neighbors_for_index(index).
        """
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index):
        """
        Returns:
          All edges for the vertex at the given index.
        """
        return self.edges[index]

    def edges_for_vertex(self, vertex):
        """
        Locate the index of the given vertex. This function passes index
        to the helper function edges_for_index(index).
        """
        return self.edges_for_vertex(self.index_of(vertex))

    def __str__(self):
        desc = ""
        for i in range(self.vertices_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc
