

def reach_target_volume(size_container_A, size_container_B, target_volume):
    """ Treat each state of the jugs as a vertex (m, n), where m and n are the amounts of
water in the jugs. Operations (filling, pouring, emptying) are edges between states. Use
Breadth-First Search (BFS) to find the shortest path from the initial state (0, 0) to the
target state (x, y) or return ”unreachable """

    start_node = (0,0)

    discovered = []
    queue = []

    graph = {}
    graph[start_node] = []

    queue.append(start_node)
    discovered.append(start_node)
    

    while len(queue) > 0:
        current_node = queue.pop()
        graph.update({current_node : []})
        if current_node == target_volume:
            path = generate_path(graph, current_node)
            path.reverse()
            path.append(current_node)
            return path
        for edge in generate_nodes(size_container_A, size_container_B, current_node):
            if edge not in discovered:
                graph[current_node].append(edge)
                discovered.append(edge)
                queue.append(edge)
    return []


def generate_path(graph, target_node):
    current_node = target_node
    path = []
    while current_node != (0,0):
        for key in graph:
            for node in graph[key]:
                if node == current_node:
                    path.append(key)
                    current_node = key
    return path
    

def generate_nodes(size_container_A, size_container_B, current_node):
    node_list = []
    node_list.append((size_container_A, current_node[1])) #fill right jug
    node_list.append((current_node[0], size_container_B)) #fill left jug
    node_list.append((0, current_node[1]))
    node_list.append((current_node[0], 0))
    temp_jug_A = current_node[0]
    temp_jug_B = current_node[1]

    #pour into container A
    while temp_jug_A < size_container_A and temp_jug_B > 0:
        temp_jug_A += 1
        temp_jug_B -= 1
    node_list.append((temp_jug_A,temp_jug_B))
    temp_jug_A = current_node[0]
    temp_jug_B = current_node[1]

    #pour into container B
    while temp_jug_A > 0 and temp_jug_B < size_container_B:
        temp_jug_A -= 1
        temp_jug_B += 1
    node_list.append((temp_jug_A,temp_jug_B))
    return node_list

if __name__ == "__main__":
    print(reach_target_volume(5, 3, (4,0)))