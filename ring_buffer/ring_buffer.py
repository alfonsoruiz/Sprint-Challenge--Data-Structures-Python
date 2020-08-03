class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.loc = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
            self.loc += 1
        elif self.loc >= self.capacity:
            self.data.pop(0)
            self.data.insert(0, item)
            self.loc = 1
        else:
            self.data.pop(self.loc)
            self.data.insert(self.loc, item)
            self.loc += 1

    def get(self):
        return self.data
