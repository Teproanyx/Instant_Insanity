from dice import Dice
from typing import List
import igraph as ig
import matplotlib.pyplot as plt


def graph_solution(die: List[Dice], colors: List[str]):
    dice_id = [i for j in range(1, 5) for i in [j]*3]
    edges = [d for dices in die for d in dices.to_edge()]

    g = ig.Graph(n=4, vertex_attrs={"name": colors})
    g.add_edges(edges)
    g.es['id'] = dice_id

    visual_style = {"layout": g.layout_grid(), "margin": 100, "edge_width": [1 + 2*(n-1) for n in dice_id],
                    "edge_color": [edge_to_color(e) for e in dice_id]}
    # fig, ax = plt.subplots()
    # ig.plot(g, target=ax, layout=layout, margin=200)
    # plt.show()
    ig.plot(g, target='test.svg', **visual_style)


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
