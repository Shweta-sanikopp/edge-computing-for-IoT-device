class EdgeNode:

    def __init__(self, edge_id, x, y):

        self.edge_id = edge_id
        self.x = x
        self.y = y

    def __repr__(self):
        return self.edge_id