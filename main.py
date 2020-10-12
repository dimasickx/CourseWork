import copy


stop_recursion = None


def main():
    n = int(input())
    graph = set_graph(n)
    visited = [False for _ in range(n)]
    color_list = [set(), set()]
    dfs(graph, color_list, visited, 1, 'red')
    if stop_recursion:
        print(-1)
        return
    result = ''
    red, blue = set(color_list[0]), set(color_list[1])
    for i in range(n + 1):
        if i in red:
            result += '0'
        elif i in blue:
            result += '1'
    print(result)


def set_graph(n: int):
    graph = dict()
    for i in range(n):
        graph[i + 1] = set()
    for i in range(n):
        for edge in input().split():
            if int(edge) != 0:
                graph[i + 1].add(int(edge))
                graph[int(edge)].add(i + 1)
    return graph


def dfs(graph, color_list, visited, k, color):
    global stop_recursion
    if color == 'red':                                 # red
        visited[k - 1] = True
        color_list[0].add(k)
        for j in graph[k]:
            if j in color_list[0]:
                stop_recursion = True
            color_list[1].add(j)               # add to blue
        for e in color_list[1]:
            if e in color_list[0]:
                stop_recursion = True
        for nk in copy.copy(color_list[1]):
            if not visited[nk - 1] and stop_recursion is None:
                dfs(graph, color_list, visited, nk, 'blue')
    else:                                          # blue
        visited[k - 1] = True
        color_list[1].add(k)
        for j in graph[k]:
            if j in color_list[1]:
                stop_recursion = True
            color_list[0].add(j)                # add ro red
        for e in color_list[0]:
            if e in color_list[1]:
                stop_recursion = True
        for nk in copy.copy(color_list[0]):
            if not visited[nk - 1] and stop_recursion is None:
                dfs(graph, color_list, visited, nk, 'red')


if __name__ == '__main__':
    main()
