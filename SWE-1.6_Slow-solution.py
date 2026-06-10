import heapq


class MedianFinder:
    def __init__(self):
        self.bottom = []  # max-heap
        self.top = []  # min-heap

    def addNum(self, num: int) -> None:
        if len(self.bottom) == len(self.top):
            heapq.heappush(self.top, -heapq.heappushpop(self.bottom, -num))
        else:
            heapq.heappush(self.bottom, -heapq.heappushpop(self.top, num))

    def findMedian(self) -> float:
        if len(self.bottom) == len(self.top):
            return float(self.top[0] - self.bottom[0]) / 2.0
        else:
            return float(self.top[0])
