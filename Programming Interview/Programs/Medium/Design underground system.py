class UndergroundSystem:

    def __init__(self):
        self.a = []
        self.b = []

    def checkIn(self, id, stationName, t):
        self.a.append([id, stationName, t])

    def checkOut(self, id, stationName, t):
        self.b.append([id, stationName, t])

    def getAverageTime(self, startStation, endStation):
        count = 0
        sum = 0
        for items in self.a:
            for data in self.b:
                if items[0] == data[0]:
                    if items[1] == startStation:
                        if data[1] == endStation:
                            count += 1
                            sum += (data[2] - items[2])
        return (sum / count)

obj = UndergroundSystem()
obj.checkIn(45, "Leyton", 3)
obj.checkIn(32, "Paradise", 8)
obj.checkIn(27, "Leyton", 10)
obj.checkOut(45, "Waterloo", 15)
obj.checkOut(27, "Waterloo", 20)
obj.checkOut(32, "Cambridge", 22)
print (obj.getAverageTime("Paradise", "Cambridge"))
print (obj.getAverageTime("Leyton", "Waterloo"))
obj.checkIn(10, "Leyton", 24)
print (obj.getAverageTime("Leyton", "Waterloo"))
obj.checkOut(10, "Waterloo", 38)
print (obj.getAverageTime("Leyton", "Waterloo"))