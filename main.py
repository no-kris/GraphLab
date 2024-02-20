import csv
from graph import Graph
from generic_search import bfs, node_to_path, dfs


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

def get_cities_from_user():
    from_city = input("Enter city departure: ").strip().lower().title()
    to_city = input("Enter city destination: ").strip().lower().title()
    return from_city, to_city

def get_choice_from_user():
    user_choice = int(input("""\nChoose one of the options below
                            \n 1. Use breadth-first search
                            \n 2. Use depth-first search 
                            \n 3. To quit program.
                            \n Enter choice: """))
    return user_choice

def display_path(path, label):
    if path is None:
        print(f"No solution found using {label}.")
    else:
        valid_path = node_to_path(path)
        print(f"\nFound path using {label}")
        print(valid_path)
        print()

if __name__ == '__main__':
    city_graph = create_graph_from_csv('cities.csv')
    # print(city_graph) # Prints the name of the city and its connected edges (cities).

    while True:
        from_city, to_city = get_cities_from_user()
        search_choice = get_choice_from_user()
        if search_choice == 1:
            bfs_result = bfs(from_city, lambda x: x == to_city, city_graph.neighbors_for_vertex)
            display_path(bfs_result, "breadth-first search")
        elif search_choice == 2:
            dfs_result = dfs(from_city, lambda x: x == to_city, city_graph.neighbors_for_vertex)
            display_path(dfs_result, "depth-first search")
        elif search_choice == 3:
            print("Ok, program now ending. Bye!\n")
            break
        else:
            print("Sorry, that was not a valid option.")
        go_again = input("\nWould you like to go again (Y/n): ").upper()
        if go_again == "N":
            print("Ok, program now ending. Bye!\n")
            break

