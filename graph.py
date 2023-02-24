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
    mg.es['id'] = dice_id

    print_multigraph(dice_id, mg)


def print_multigraph(dice_id, mg):
    visual_style = {"layout": mg.layout_grid(), "margin": 100, "edge_width": [1 + 2 * (n - 1) for n in dice_id],
                    "edge_color": [edge_to_color(e) for e in dice_id]}
    ig.plot(mg, target='test.svg', **visual_style)


def edge_to_color(edge: int) -> str:
    match edge:
        case 1:
            return 'red'
        case 2:
            return 'blue'
        case 3:
            return 'green'
        case _:
            return 'black'
