import itertools
from dice import Dice
from typing import List, Tuple
import igraph as ig


def graph_solution(die: List[Dice], colors: List[str]) -> List[List[Dice]]:
    edges = [dices.to_edge() for dices in die]

    g = [ig.Graph(n=len(colors), vertex_attrs={"name": colors}) for i in range(len(edges))]
    for i, (graph, edge_list) in enumerate(zip(g, edges)):
        graph.add_edges(edge_list)
        graph.es['id'] = i + 1

    mg = ig.Graph(n=4, vertex_attrs={"name": colors})
    mg.add_edges([edge for each_edge in edges for edge in each_edge])

    dice_id = [i for j in range(1, len(edges) + 1) for i in [j] * 3]
    mg.es["id"] = dice_id

    print_graph_list(g, 'cube')
    print_graph(mg, "multigraph")

    filtered_subgraph = get_subgraph_deg2(g, colors)
    print_graph_list(filtered_subgraph, 'subgraph')

    solution_set = non_overlapping_graphs(filtered_subgraph, colors)

    dice_solution = []
    for i, solution in enumerate(solution_set):
        print_graph_list(list(solution), "solution" + str(i+1) + " set")
        dice_solution.append(dgraph_to_dices(*solution))

    return dice_solution


def dgraph_to_dices(dgraph1: ig.Graph, dgraph2: ig.Graph) -> List[Dice]:
    dices = []
    for front_back, left_right in zip(dgraph1.es, dgraph2.es):
        front = dgraph1.vs[front_back.source]["name"]
        back = dgraph1.vs[front_back.target]["name"]
        left = dgraph2.vs[left_right.source]["name"]
        right = dgraph2.vs[left_right.target]["name"]

        dices.append(Dice(["X", left, front, right, "X", back]))

    return dices


def non_overlapping_graphs(subgraph: List[ig.Graph], colors: List[str]) -> List[Tuple[ig.Graph, ig.Graph]]:
    no_overlap_union = []
    for subgraph1, subgraph2 in itertools.combinations(subgraph, 2):
        if not is_overlapping(subgraph1, subgraph2):
            directed_subgraph1 = get_directed_graph(subgraph1)
            directed_subgraph2 = get_directed_graph(subgraph2)
            no_overlap_union.append((directed_subgraph1, directed_subgraph2))
    return no_overlap_union


def get_directed_graph(g: ig.Graph) -> ig.Graph:
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
    return any((e1 == e2 for e1, e2 in zip(graph1.get_edgelist(), graph2.get_edgelist())))


def get_subgraph_deg2(graph: List[ig.Graph], colors: List[str]) -> List[ig.Graph]:
    subgraph = [ig.Graph(n=len(colors), vertex_attrs={"name": colors}, edges=edge_list,
                         edge_attrs={"id": [i + 1 for i in range(len(edge_list))]})
                for edge_list in itertools.product(*[graph.get_edgelist() for graph in graph])]
    return [graph for graph in subgraph if all((vertex.degree() == 2 for vertex in graph.vs))]


def print_graph_list(graphs: List[ig.Graph], output: str):
    for i, graph in enumerate(graphs):
        print_graph(graph, output + str(i + 1))


def print_graph(graph: ig.Graph, output: str):
    visual_style = {"layout": graph.layout_grid(), "margin": 100,
                    "vertex_label": [color for color in graph.vs["name"]],
                    "vertex_label_size": 30,
                    "vertex_color": [vertex_name_to_color(v) for v in graph.vs["name"]],
                    "vertex_size": 50,
                    "vertex_shape": "rectangle",
                    "edge_label": [dice_id for dice_id in graph.es["id"]],
                    "edge_width": [dice_id + 1 for dice_id in graph.es["id"]],
                    "edge_color": [dice_id_to_color(dice_id) for dice_id in graph.es["id"]]}
    ig.plot(graph, target=output + '.svg', **visual_style)


def vertex_name_to_color(edge: str) -> str:
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


def dice_id_to_color(d_id: int) -> str:
    match d_id:
        case 1:
            return 'cyan'
        case 2:
            return 'magenta'
        case 3:
            return 'yellow'
        case _:
            return 'black'
