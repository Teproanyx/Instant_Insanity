import itertools
from dice import Dice
from typing import List
import igraph as ig


def graph_solution(die: List[Dice], colors: List[str]):
    edges = [dices.to_edge() for dices in die]

    g = [ig.Graph(n=4, vertex_attrs={"name": colors}) for i in range(len(edges))]
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

    for subgraph1, subgraph2 in itertools.combinations(filtered_subgraph, 2):
        pass  # TODO


def get_subgraph_deg2(graph: List[ig.Graph], colors: List[str]):
    subgraph = [ig.Graph(n=4, vertex_attrs={"name": colors}, edges=edge_list,
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
