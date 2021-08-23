import math

class Equation:
    def __init__(self, a, b, c):
        self.a, self.b, self.c, self.delta = a, b, c, (b**2 - 4 * a * c);

    def solve(self):
        # Case 1: [Delta > 0]
        if self.delta > 0:
            x1 = ((-self.b + math.sqrt(self.delta)) / (2 * self.a));
            x2 = ((-self.b - math.sqrt(self.delta)) / (2 * self.a));

            return x1, x2


        # Case 2: [Delta = 0]
        elif self.delta == 0:
            x = ((-self.b) / (2 * self.a));

            return x


        # Case 3: [Delta < 0]
        elif self.delta < 0:
            return None
