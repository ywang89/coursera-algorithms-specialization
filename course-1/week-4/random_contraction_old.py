# This is a method I came up without using class. It's a bit of slow, but it
# does return correct results.

import random
import math
import copy


def replace(x, v_1, v_2):
    """Replace v_2 with v_1 for all lists in x.

    Args:
        x: A list of list of integers.
        v_1: An integer, value to be replaced with.
        v_2: An integer, value to replace.

    Returns:
        Nothing. Replacement happens in place.
    """
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            if x[i][j] == v_2:
                x[i][j] = v_1


def remove(x, v_1):
    """Removes in place self loops from x.
    """
    for i in range(0, len(x)):
        j = 1
        # Examine on a particular row
        while j <= len(x[i]) - 1:
            list_len = len(x[i])
            if x[i][j] == x[i][0]:
                # Below slicing works on edge case when x[i] is of length 2
                x[i][j:list_len - 1] = x[i][j + 1:]
                x[i].pop()
                j = j - 1
            j = j + 1


def aggregate(x, v_1):
    """'Aggregate' rows in x that starts with v_1.

    For example, [1,2,3] and [1,4] are aggregated to be [1,2,3,4]
    """
    new_row = [v_1]
    i = 0
    while i < len(x):
        if x[i][0] == v_1:
            new_row.extend(x[i][1:])
            x.pop(i)
            i = i - 1
        i = i + 1
    x.append(new_row)


def count_edges(x):
    """Counts the number of edges.
    """
    count = 0
    for i in range(0, len(x)):
        count = count + len(x[i]) - 1
    count = int(count / 2)  # Each edge is counted twice
    return count


def random_contraction_base(x):
    """Counts minimum cuts using random contraction algorithm.

    Args:
        x: An list of list of integers (adjacency list), representing a graph.

    Returns:
        A integer, representing the minimum cuts.
    """
    # make below work better
    assert x is not None and len(x) >= 1, "Invalid input."

    while len(x) > 2:
        # selects an edge randomly.
        i_1 = random.randint(0, len(x)-1)
        j_1 = random.randint(1, len(x[i_1])-1)

        v_1 = x[i_1][0]
        v_2 = x[i_1][j_1]

        # replace v_2 with v_1 for all rows
        replace(x, v_1, v_2)
        # remove self loops
        remove(x, v_1)
        # "aggregate" based on the first element
        aggregate(x, v_1)
    # count edges
    min_cut_count = count_edges(x)
    return min_cut_count


def random_contraction(x, trial_number):
    """Calculates min cut count using random contraction with repeated trials.

    When the number of trials is n*n*ln(n), probability of all failing is <=
    1 / n; when the number of trials is n*n, probability of all failing is <=
    1 / e.
    """
    i = 0
    min_cut_count = float("inf")
    while i < trial_number:
        min_cut_count_tmp = random_contraction_base(copy.deepcopy(x))
        # Keep smallest min cut count.
        if min_cut_count_tmp < min_cut_count:
            min_cut_count = min_cut_count_tmp
        i = i + 1
    return min_cut_count


def alg(file_path):
    f = open(file_path, 'r')
    graph = []
    for line in f:
        tmp = line.rstrip()
        tmp = tmp.replace(' ', '\t')
        tmp = tmp.split('\t')
        graph.append(tmp)
    f.close()

    n = len(graph)
    trial_number = int(n*n*math.log(n))
    min_cut = random_contraction(graph, trial_number=trial_number)
    return min_cut
