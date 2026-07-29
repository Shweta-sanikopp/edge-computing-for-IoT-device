class Batching:

    def __init__(self):

        self.buffer = []

    def execute(self, packet):

        self.buffer.append(packet)

        if len(self.buffer) >= 10:

            batch = self.buffer.copy()

            self.buffer.clear()

            return batch

        return None