class UndergroundSystem:
    def __init__(self):
        self.checkinMap = {} # id -> (start, end)
        self.totalMap = {} # (start, end) -> [total_time, count]
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinMap[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkinMap[id]
        route = (start, stationName)

        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]

        self.totalMap[route][0] += t - time
        self.totalMap[route][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count
    

