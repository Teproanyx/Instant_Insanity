import itertools
from typing import List, Tuple

import igraph as ig

from cube import Cube


def graph_solution(cube: List[Cube], colors: List[str]) -> List[List[Cube]]:
    """Given the set of Cube and colors of the faces, find the list of solution in the form of 4 set of Cube"""
    # Turn cube to edge list
    edges = [c.to_edgelist() for c in cube]

    # Create each cube sub graph and give them their cube no. as id
    g = [ig.Graph(n=len(colors), vertex_attrs={"name": colors}) for i in range(len(edges))]
    for i, (graph, edge_list) in enumerate(zip(g, edges)):
        graph.add_edges(edge_list)
        graph.es['id'] = i + 1

    # Create the fused multigraph of the four cube and assign the edge their id
    mg = ig.Graph(n=4, vertex_attrs={"name": colors})
    mg.add_edges([edge for each_edge in edges for edge in each_edge])
    cube = [i for j in range(1, len(edges) + 1) for i in [j] * 3]
    mg.es["id"] = cube

    # Output the graphs
    print_graph_list(g, "cube")
    print_graph(mg, "multigraph")

    # Get the subgraphs with vertices degree of 2 and edges with unique id(edges from different cube)
    filtered_subgraph = get_subgraph_deg2(g, colors)
    print_graph_list(filtered_subgraph, 'subgraph')

    # Get pairs of subgraphs who don't overlap with each other
    solution_set = non_overlapping_graphs(filtered_subgraph)

    # Output each set of solution subgraphs and turn them back to Cube object
    cube_solutions = []
    for i, solution in enumerate(solution_set):
        print_graph_list(list(solution), "solution" + str(i + 1) + " set")
        cube_solutions.append(dgraph_to_cube(*solution))

    return cube_solutions


def dgraph_to_cube(dgraph1: ig.Graph, dgraph2: ig.Graph) -> List[Cube]:
    """Turn directed graph into set of 4 Cube object with unknown up or down face"""
    cubes = []
    for front_back, left_right in zip(dgraph1.es, dgraph2.es):
        front = dgraph1.vs[front_back.source]["name"]
        back = dgraph1.vs[front_back.target]["name"]
        left = dgraph2.vs[left_right.source]["name"]
        right = dgraph2.vs[left_right.target]["name"]

        cubes.append(Cube(["X", left, front, right, "X", back]))

    return cubes


def print_graph_list(graphs: List[ig.Graph], output: str):
    """print_graph but with indexing output for list"""
    for i, graph in enumerate(graphs):
        print_graph(graph, output + str(i + 1))


def print_graph(graph: ig.Graph, output: str):
    """Draw the graph object and plot it to output.svg"""
    visual_style = {"layout": graph.layout_grid(), "margin": 100,
                    "vertex_label": [color for color in graph.vs["name"]],
                    "vertex_label_size": 30,
                    "vertex_color": [vertex_name_to_color(v) for v in graph.vs["name"]],
                    "vertex_size": 50,
                    "vertex_shape": "rectangle",
                    "edge_label": [cube_id for cube_id in graph.es["id"]],
                    "edge_width": [cube_id + 1 for cube_id in graph.es["id"]],
                    "edge_color": [cube_id_to_color(cube_id) for cube_id in graph.es["id"]]}
    ig.plot(graph, target=output + '.svg', **visual_style)


def non_overlapping_graphs(subgraph: List[ig.Graph]) -> List[Tuple[ig.Graph, ig.Graph]]:
    """Get pairs of subgraphs combination that don't overlap each other based on edge attributes from a list"""
    no_overlap_graphs = []
    for subgraph1, subgraph2 in itertools.combinations(subgraph, 2):
        if not is_overlapping(subgraph1, subgraph2):
            directed_subgraph1 = get_directed_cyclic_graph(subgraph1)
            directed_subgraph2 = get_directed_cyclic_graph(subgraph2)
            no_overlap_graphs.append((directed_subgraph1, directed_subgraph2))
    return no_overlap_graphs


def get_directed_cyclic_graph(g: ig.Graph) -> ig.Graph:
    """Turn an undirected graph into a directed cyclic graph"""
    directed_graph = ig.Graph(n=g.vcount(), vertex_attrs={"name": [v["name"] for v in g.vs]}, directed=True)
    for edge in g.es:
        if directed_graph.vs[edge.source].outdegree() == 0 and directed_graph.vs[edge.target].indegree() == 0:
            directed_graph.add_edge(edge.source, edge.target)
        elif directed_graph.vs[edge.target].outdegree() == 0 and directed_graph.vs[edge.source].indegree() == 0:
            directed_graph.add_edge(edge.target, edge.source)
        else:
            successor = directed_graph.vs[edge.target].successors()[0]
            directed_graph.add_edge(successor, edge.target)
            directed_graph.delete_edges(edge.target, successor)
            directed_graph.add_edge(edge.target, edge.source)

    directed_graph.es['id'] = list(range(1, len(g.es) + 1))
    return directed_graph


def is_overlapping(graph1: ig.Graph, graph2: ig.Graph) -> bool:
    """Given 2 graphs, find if edges with the same index intersect"""
    return any((e1 == e2 for e1, e2 in zip(graph1.get_edgelist(), graph2.get_edgelist())))


def get_subgraph_deg2(graph: List[ig.Graph], colors: List[str]) -> List[ig.Graph]:
    """Generate all subgraphs where every vertex have a degree of 2"""
    subgraph = [ig.Graph(n=len(colors), vertex_attrs={"name": colors}, edges=edge_list,
                         edge_attrs={"id": [i + 1 for i in range(len(edge_list))]})
                for edge_list in itertools.product(*[graph.get_edgelist() for graph in graph])]
    return [deg2_graph for deg2_graph in subgraph if all((vertex.degree() == 2 for vertex in deg2_graph.vs))]


def vertex_name_to_color(edge: str) -> str:
    """Return color based on string used as vertex name"""
    match edge:
        case 'R':
            return 'red'
        case 'B':
            return 'blue'
        case 'G':
            return 'green'
        case 'W':
            return 'white'
        case 'Y':
            return 'yellow'
        case _:
            return 'black'


def cube_id_to_color(d_id: int) -> str:
    """Return color based on cube for better contrast in graph visualization"""
    match d_id:
        case 1:
            return 'cyan'
        case 2:
            return 'magenta'
        case 3:
            return 'wheat'
        case _:
            return 'black'
