from collections import deque

graph = {
    'Ostrava': ['Olomouc', 'Liberec'],
    'Liberec': ['Ostrava', 'Praha'],
    'Praha': ['Liberec', 'Plzeň', 'Brno', 'České Budějovice'],
    'Brno': ['Praha'],
    'Olomouc': ['Ostrava', 'Brno'],
    'České Budějovice': ['Praha', 'Plzeň'],
    'Plzeň': ['Praha', 'České Budějovice']
}


def bfs(graph, start):
    visited = set()
    result = {}
    queue = deque([(start, 0)])
    visited.add(start)
    while queue:
        vertex, dist = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist+1))
                result[neighbor] = dist
    return result


start_city = 'Ostrava'
reachable_cities = bfs(graph, start_city)

cities_in_order = ['Praha', 'Liberec', 'Plzeň', 'České Budějovice', 'Brno', 'Olomouc']

print(f'Z města {start_city} jsou dosažitelná tato města:')
for city in cities_in_order:
    if city in reachable_cities:
        distance = reachable_cities[city]
        if distance == 0:
            print(f'         {city} je přímo spojené s městem {start_city}.')
        else:
            print(f'         {city} je dosažitelné přes {distance} měst.')