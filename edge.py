from dataclasses import dataclass


@dataclass
class Edge:
    """
    Edge class represents an edge between two vertices in a graph.
    """
    from_u: int
    to_v: int

    def reversed_edge(self):
        """
        Reverse the edge between two vertices.
        :return: Reversed edge.
        """
        return Edge(self.to_v, self.from_u)

    def __str__(self):
        return f"Edge(u={self.from_u}, v={self.to_v})"