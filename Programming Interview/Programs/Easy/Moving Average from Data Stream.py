size = 3

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def next(self, val):
        self.queue.append(val)
        sum = 0
        if len(self.queue) <= self.size:
            for i in range(len(self.queue)):
                sum += self.queue[i]
            return (sum / len(self.queue))
        else:
            for i in range(len(self.queue)-self.size, len(self.queue)):
                sum += self.queue[i]
            return (sum / self.size)

obj = MovingAverage(size)
print (obj.next(1))
print (obj.next(10))
print (obj.next(3))
print (obj.next(5))
print (obj.next(6))
print (obj.next(10))
