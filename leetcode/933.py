class RecentCounter:
    def __init__(self):
        self.requests = deque()
        self.counter = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.counter += 1

        r1 = t-3000
        while r1 > self.requests[0]:
            if r1 > self.requests[0]:
                self.counter -= 1
                self.requests.popleft()
        
        return self.counter
# Your RecentCounter object will be instantiated and called as such:
#obj = RecentCounter()
#param_1 = obj.ping(t)
