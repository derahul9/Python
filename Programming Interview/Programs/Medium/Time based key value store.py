class TimeMap:
    def __init__(self):
        self.a = []
        self.b = []

    def set(self, key, value, timestamp):
        self.a.append([key, value, timestamp])
        self.b = sorted(self.a, key = lambda P: P[2], reverse=True)

    def get(self, key, timestamp):
        for items in self.b:
            if items[0] == key:
                return items[1]
        return ""

z = TimeMap()
z.set("foo", "bar", 1)
print (z.get("foo",1))