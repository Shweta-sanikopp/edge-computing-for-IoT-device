import math


def calculate_distance(device, edge):

    return math.sqrt(

        (device.x-edge.x)**2 +

        (device.y-edge.y)**2

    )


def assign_nearest_edge(device, edge_nodes):

    nearest = min(

        edge_nodes,

        key=lambda edge: calculate_distance(device, edge)

    )

    device.edge_node = nearest.edge_id

    device.distance = calculate_distance(device, nearest)

    return device