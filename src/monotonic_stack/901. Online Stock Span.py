class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))

        return span
