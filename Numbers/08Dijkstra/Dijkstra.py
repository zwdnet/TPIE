# -*- coding:utf-8 -*-
# http://blog.csdn.net/yettocome/article/details/12584663


def get_graph():
    filename = "data.txt"
    graph = {}
    with open(filename) as g:
        for line in g:
            l = line.split()
            vertex = int(l.pop(0))
            graph[vertex] = {}
            for x in l:
                adj_vert, distance = map(int, x.split(","))
                graph[vertex][adj_vert] = distance
    print("Got graph. Ex: line 1:", graph[1])
    return graph


def dijkstra_score(G, shortest_distances, v, w):
    return shortest_distances[v] + G[v][w]


def dijkstra(G, source):
    unprocessed = set(G.keys())
    unprocessed.remove(source)
    shortest_distances = {source: 0}

    for i in range(len(G) - 1):
        m, closest_head = float('inf'), 0
        for tail in shortest_distances:
            for head in G[tail]:
                if head in unprocessed:
                    d = dijkstra_score(G, shortest_distances, tail, head)
                    if d < m:
                        m, closest_head = d, head

        unprocessed.remove(closest_head)

    for vertex in unprocessed:
        shortest_distances[vertex] = float('inf')

    return shortest_distances


def main():
    G = get_graph()
    source = int(input("Enter source vertex:"))
    destination_vvertices = map(int, input("List destination vertices:\n").split())

    distances = dijkstra(G, source)



if __name__ == '__main__':
    main()