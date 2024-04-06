class RecentCounter:
    def __init__(self):
        self.requests = deque()
        self.len_req = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.len_req = len(self.requests)
        r1 = t-3000
        for req in self.requests:
            if r1 > req:
                self.len_req -= 1
            else:
                break
        return self.len_req
