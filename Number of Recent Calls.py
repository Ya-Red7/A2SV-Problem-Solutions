class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        self.q.append(t)
        while t - self.q[0] > 3000:
            self.q.pop(0)
        return len(self.q)
