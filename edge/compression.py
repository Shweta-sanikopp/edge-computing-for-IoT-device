import json
import gzip


class Compression:

    def execute(self, packet):

        if packet is None:
            return None

        data = json.dumps(packet).encode()

        compressed = gzip.compress(data)

        return compressed