import heapq

def dijkstra(graph, start):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        (dist, current) = heapq.heappop(heap)
        if dist > distances[current]:
            continue
        for neighbor, weight in graph[current].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances


graph = {
'Ostrava': {'Olomouc': 84, 'Liberec': 340},
'Liberec': {'Ostrava': 340, 'Praha': 75},
'Praha': {'Liberec': 75, 'Plzeň': 120, 'Brno': 186, 'České Budějovice': 77, 'Olomouc': 252},
'Brno': {'Praha': 186, 'Olomouc': 95},
'Olomouc': {'Ostrava': 84, 'Brno': 95, 'Praha':252},
'České Budějovice': {'Praha': 77, 'Plzeň': 92},
'Plzeň': {'Praha': 120, 'České Budějovice': 92}
}

start_city = 'Ostrava'
city_order = ['Ostrava', 'Praha', 'Liberec', 'Plzeň', 'České Budějovice', 'Brno', 'Olomouc']

distances = dijkstra(graph, start_city)

print(f'Od města {start_city} jsou ostatní města vzdálená:')
for city in sorted(distances.keys(), key=lambda x: city_order.index(x)):
    if city != start_city:
        print(f'{city} {distances[city]} km.')