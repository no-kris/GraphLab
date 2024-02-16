import csv
from graph import Graph


def create_graph_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        edges = [(row[0], row[1]) for row in reader]

    vertices = set()
    for edge in edges:
        vertices.update(edge)

    graph = Graph(list(vertices))
    for source, target in edges:
        graph.add_edge_by_vertices(source, target)
    return graph


if __name__ == '__main__':
    city_graph = create_graph_from_csv('cities.csv')
    print(city_graph)
