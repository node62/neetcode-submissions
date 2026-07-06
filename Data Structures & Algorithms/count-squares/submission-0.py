class CountSquares:
    def __init__(self):
        self.xcor = {}
        self.ycor = {}

    def add(self, point: List[int]) -> None:
        x, y = point

        # xcor
        if x not in self.xcor:
            self.xcor[x] = {}
        if y not in self.xcor[x]:
            self.xcor[x][y] = 1
        else:
            self.xcor[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point

        ans = 0
        if x in self.xcor:
            for y_ in self.xcor[x]:
                if y_ == y:
                    continue

                temp = self.xcor[x][y_]
                dist = abs(y_ - y)

                if self.exists(x - dist, y_):
                    if self.exists(x - dist, y):
                        ans += (
                            self.xcor[x][y_] *
                            self.xcor[x-dist][y_] *
                            self.xcor[x-dist][y]
                        )
                if self.exists(x + dist, y_):
                    if self.exists(x + dist, y):
                        ans += (
                            self.xcor[x][y_] *
                            self.xcor[x+dist][y_] *
                            self.xcor[x+dist][y]
                        )

        return ans
    
    def exists(self, x, y):
        if x in self.xcor and y in self.xcor[x]:
            return True
        return False