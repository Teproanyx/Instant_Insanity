import itertools


def edge_solution(list_of_dice: list) -> list:
    # first_list = [(4, 3), (1, 2), (2, 3, 4), (1, 3)]

    # second_list = [p for p in itertools.product(*first_list) if is_unique(p)]
    # print(second_list)
    list_of_edge = [x.to_edge() for x in list_of_dice]
    # print(list_of_edge)

    # list_of_opposite_edge = [[(v, k) for (k, v) in x] for x in list_of_edge]
    # print(list_of_opposite_edge)
    list_of_directed_edge = [set(x + [(v, k) for (k, v) in x]) for x in list_of_edge]
    # print(list_of_directed_edge)

    permutation = [p for p in itertools.product(*list_of_directed_edge) if node_degree_check(p)]
    # print(permutation)

    passed = []
    while permutation:
        current_per = permutation.pop()
        for perm in permutation:
            new_perm = {current_per, perm}
            if not same_edge_in_edge_set(current_per, perm) \
                    and not any(is_duplicate(new_perm, completed_set) for completed_set in passed):
                passed.append(new_perm)

    return passed


def is_unique(lis) -> bool:
    return len(lis) == len(set(lis))


def node_degree_check(lis) -> bool:
    left = [k for (k, v) in lis]
    right = [v for (k, v) in lis]
    return is_unique(left) and is_unique(right)


def same_edge_in_edge_set(edge_set_1: tuple, edge_set_2: tuple) -> bool:
    for x, y in zip(edge_set_1, edge_set_2):
        if same_edge(x, y):
            return True

    return False


def same_edge(edge_1: tuple, edge_2: tuple) -> bool:
    return edge_1 == edge_2 or edge_1 == (edge_2[1], edge_2[0])


def is_duplicate(set1: set, set2: set) -> bool:
    return all(same_edge(a, b) for x, y in zip(set1, set2) for a, b in zip(x, y))
