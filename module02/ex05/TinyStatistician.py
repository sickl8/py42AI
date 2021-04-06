class TinyStatistician:
    def __init__(self):
        return

    def mean(self, x):
        if len(x) == 0:
            return None
        mean = 0
        for num in x:
            mean += num
        mean = mean / len(x)
        return float(mean)

    def median(self, x):
        if len(x) == 0:
            return None
        x.sort()
        ln = len(x) - 1
        if len(x) % 2 == 0:
            median = (x[int(ln / 2)] + x[int(ln / 2 + 1)]) / 2
        else:
            median = x[int((ln + 1) / 2)]
        return float(median)

    def quartile(self, x, percentile):
        if len(x) == 0 or (percentile != 25 and percentile != 75):
            return None
        if self.median(x) not in x:
            x.append(self.median(x))
        x.sort()
        lower = x[:x.index(self.median(x)) + 1]
        higher = x[x.index(self.median(x)):]
        if percentile == 75:
            return self.median(higher)
        return self.median(lower)

    def var(self, x):
        if len(x) == 0:
            return None
        m = float(len(x))
        mean = self.mean(x)
        varsqr = sum(float(num_i - mean) ** 2 for num_i in x) / m
        return varsqr

    def std(self, x):
        if len(x) == 0:
            return None
        return self.var(x) ** 0.5


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
print(tstat.median(a))
print(tstat.quartile(a, 25))
print(tstat.quartile(a, 75))
print(tstat.var(a))
print(tstat.std(a))
