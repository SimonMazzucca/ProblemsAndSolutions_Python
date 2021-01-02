class LC0050_Pow:
    def myPow(self, x: float, n: int) -> float:
        N = n

        if N < 0:
            x = 1 / x
            N = -N

        return self.fastPower(x, N)

    def fastPower(self, x, n) -> float:
        if n == 0:
            return 1

        half = self.fastPower(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
