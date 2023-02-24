from dice import Dice
from typing import List
import igraph as ig


def graph_solution(die: List[Dice], colors: List[str]):
    edges = [dices.to_edge() for dices in die]

    g = [ig.Graph(n=4, vertex_attrs={"name": colors}) for i in range(len(edges))]
    for graph, edge_list in zip(g, edges):
        graph.add_edges(edge_list)

    mg = ig.Graph(n=4, vertex_attrs={"name": colors})
    mg.add_edges([edge for each_edge in edges for edge in each_edge])

    dice_id = [i for j in range(1, len(edges)) for i in [j] * 3]
    mg.es["id"] = dice_id

    print_graph_list(g, 'cube')
    print_multigraph(mg)


def print_graph_list(graphs: List[ig.Graph], out_filename):
    for i, graph in enumerate(graphs):
        visual_style = {"layout": graph.layout_grid(), "margin": 50,
                        "vertex_label": [color for color in graph.vs["name"]],
                        "vertex_color": [vertex_name_to_color(v) for v in graph.vs["name"]]}
        ig.plot(graph, target=out_filename + str(i + 1) + '.svg', **visual_style)


def print_multigraph(multigraph):
    visual_style = {"layout": multigraph.layout_grid(), "margin": 100,
                    "vertex_label": [color for color in multigraph.vs["name"]],
                    "vertex_color": [vertex_name_to_color(v) for v in multigraph.vs["name"]],
                    "edge_label": [dice_id for dice_id in multigraph.es["id"]],
                    "edge_width": [dice_id + 1 for dice_id in multigraph.es["id"]],
                    "edge_color": [dice_id_to_color(dice_id) for dice_id in multigraph.es["id"]]}
    ig.plot(multigraph, target='multigraph.svg', **visual_style)


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
