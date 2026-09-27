# Advent of Code
# Year: 2015
# Day: 9

from pathlib import Path
from itertools import permutations

def read_input():
    return Path("./python/input.txt").read_text().splitlines()

def parse_input(line):
    info = line.split(" ")
    return info[0], info[2], info[4]

def create_graph(data):
    graph = dict()
    for line in data:
        A, B, distance = parse_input(line)
        
        if A not in graph:
            graph[A] = {}
        if B not in graph:
            graph[B] = {}
        
        graph[A][B] = int(distance)
        graph[B][A] = int(distance)

    return graph

def route_distance(route, graph):
    total = 0;

    for i in range(len(route) - 1):
        a, b = route[i], route[i - 1]
        total += graph[a][b]

    return total

def part1(data):
    graph = create_graph(data)
    locations = list(graph.keys())
    routes = permutations(locations)

    minimum_distance = None
    for route in routes:
        distance = route_distance(route, graph)
        if minimum_distance is None or distance < minimum_distance:
            minimum_distance = distance

    return minimum_distance

def part2(data):
    # Solve Part 2
    pass

def main():
    data = read_input()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

if __name__ == "__main__":
    main()