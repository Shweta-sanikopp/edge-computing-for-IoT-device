from edge.filtering import Filtering

from edge.aggregation import Aggregation

from edge.batching import Batching

from edge.compression import Compression

from edge.encryption import Encryption

from edge.metrics import Metrics


class EdgeGateway:

    def __init__(self, edge_id):

        self.edge_id = edge_id

        self.filter = Filtering()

        self.aggregate = Aggregation()

        self.batch = Batching()

        self.compress = Compression()

        self.encrypt = Encryption()

        self.metrics = Metrics()

    def process(self, packet):

        packet = self.filter.execute(packet)

        packet = self.aggregate.execute(packet)

        packet = self.batch.execute(packet)

        packet = self.compress.execute(packet)

        packet = self.encrypt.execute(packet)

        self.metrics.update(packet)

        return packet