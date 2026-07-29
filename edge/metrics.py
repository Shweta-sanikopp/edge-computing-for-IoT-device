class Metrics:

    def __init__(self):

        self.received = 0

        self.forwarded = 0

    def update(self, packet):

        self.received += 1

        if packet is not None:

            self.forwarded += 1