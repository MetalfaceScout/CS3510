


def min_shelves(books, pairs):
    graph = {}
    shelves = set()

    # Generate the graph in an easier way to handle
    for book in books:
        graph.update({
            book : []
        })

    for pair in pairs:
        graph.get(pair[0]).append(pair[1])
        graph.get(pair[1]).append(pair[0])


    for book in graph:
        discovered = []
        queue = []

        for node in graph[book]:
            queue.append(node)

        while len(queue) > 0:
            current_node = queue.pop()
            for edge in graph[current_node]:
                if edge not in discovered:
                    discovered.append(edge)
                    queue.append(edge)

        discovered.sort()
        if len(discovered) > 0:
            shelves.add(discovered[0])
        else:
            shelves.add(book)
    
    return len(shelves)

if __name__ == "__main__":
    books = ['u', 'v', 'w', 'x']
    pairs = [('u', 'v'), ('v', 'w')]

    print(min_shelves(books, pairs))

    books = ['a', 'b', 'c', 'd', 'e', 'f']
    pairs = [('a', 'b'), ('b', 'c'), ('d', 'e')]

    print(min_shelves(books, pairs))

    books = ['a', 'b', 'c', 'd', 'e', 'f']
    pairs = [('a', 'b'), ('b', 'c'), ('d', 'e')]

    print(min_shelves(books, pairs))