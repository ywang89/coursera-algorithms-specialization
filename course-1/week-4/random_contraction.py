# Since my own method is bit slow, I wrote the solution in another way,
# using class. I learnt the method from below repo:
# https://github.com/white105/stanford-algorithms/blob/master/Divide%20and%20Conquer%2C%20Sorting%20and%20Searching%2C%20and%20Randomized%20Algorithms/problem_sets/problem_set4/problem_4.py

import random
import math
import copy


class Adjacency:
    """Represents one element in the adjacency list.
    """
    def __init__(self, node, edge):
        self.node = node
        self.edge = edge

    def contract(self, adj):
        """Contracts another Adjacency object 'adj'
        """
        self.node += adj.node
        self.edge = [e for e in self.edge + adj.edge if e not in self.node]

    def __repr__(self):
        return '[node: {0}, edge: {1}]'.format(self.node, self.edge)


def cut(graph):
    """Contracts till there are only 2 nodes left.
    """
    while len(graph) > 2:
        rand_pick = random.choice(graph)
        merge_node = random.choice(rand_pick.edge)
        merge_pick = [i for i in graph if merge_node in i.node]
        rand_pick.contract(merge_pick[0])
        graph.remove(merge_pick[0])
    min_cut_num = len(graph[0].edge)
    return min_cut_num


def cut_min_cross(graph, trial_number):
    """Gets the min cut number via repeated trials.

    When the number of trials is n*n*ln(n), probability of all failing is <=
    1 / n; when the number of trials is n*n, probability of all failing is <=
    1 / e.
    """
    minimum = float('inf')
    i = 0
    while i < trial_number:
        min_cut_num = cut(copy.deepcopy(graph))
        if min_cut_num < minimum:
            minimum = min_cut_num
        i = i + 1
    return minimum


def alg(file_path):
    f = open(file_path, 'r')
    graph = []
    for line in f:
        tmp = line.rstrip()
        tmp = tmp.replace(' ', '\t')
        tmp = tmp.split('\t')
        graph.append(Adjacency(node=[tmp[0]], edge=tmp[1:]))
    f.close()

    n = len(graph)
    trial_number = int(n*n*math.log(n))
    min_cut = cut_min_cross(graph, trial_number=trial_number)
    return min_cut
