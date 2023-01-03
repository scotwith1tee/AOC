import sys

INF = sys.maxsize

def floyd_warshall(graph):
    source_vertices = [column[0] for column in graph]
    destination_vertices = [column[1] for column in graph]
    vertices = list(set(source_vertices) | set(destination_vertices))

    distance = [[INF] * len(vertices) for i in range(len(vertices))]
    next_vertices  = [[0]   * len(vertices) for i in range(len(vertices))]

    for i in range(len(vertices)):
        distance[i][i] = 0
    for source, destination, weight in graph:
        distance[source-1][destination-1] = weight
        next_vertices[source-1][destination-1] = destination-1

    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_vertices[i][j]  = next_vertices[i][k]

    path_reconstruction(distance, next_vertices)

def path_reconstruction(dist, nxt):
    print("Edge \t\t Distance \t Shortest Path")
    for i in range(len(dist)):
        for j in range(len(dist)):
            if i != j:
                path = [i]
                while path[-1] != j:
                    path.append(nxt[path[-1]][j])
                print("(%d, %d) \t\t %2d \t\t %s"
                      % (i + 1, j + 1, dist[i][j], ' - '.join(str(p + 1) for p in path)))
    print()

def main():
    edge_list1 = [
        [1, 3, -2],
        [2, 1, 4],
        [2, 3, 3],
        [3, 4, 2],
        [4, 2, -1]
    ]
    edge_list2 = [
        [1, 2, 10],
        [1, 3, 20],
        [1, 4, 30],
        [2, 6, 7],
        [3, 6, 5],
        [4, 5, 10],
        [5, 1, 2],
        [5, 6, 4],
        [6, 2, 5],
        [6, 3, 7],
        [6, 5, 6]
    ]

    floyd_warshall(edge_list1)
    floyd_warshall(edge_list2)

if __name__ == '__main__':
    main()