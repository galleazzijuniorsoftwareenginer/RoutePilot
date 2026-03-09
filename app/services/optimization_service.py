import math


def distance(a, b):

    lat1, lon1 = a
    lat2, lon2 = b

    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)


def optimize_route(locations):

    route = [0]

    remaining = list(range(1, len(locations)))

    while remaining:

        last = route[-1]

        next_stop = min(
            remaining,
            key=lambda x: distance(locations[last], locations[x])
        )

        route.append(next_stop)

        remaining.remove(next_stop)

    return route
