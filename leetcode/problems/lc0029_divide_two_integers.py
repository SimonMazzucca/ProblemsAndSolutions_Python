class LC0029_Divide_Two_Integers:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        negatives = 0

        if dividend < 0:
            dividend = -dividend
            negatives = negatives + 1

        if divisor < 0:
            divisor = -divisor
            negatives = negatives + 1

        while dividend - divisor >= 0:
            dividend -= divisor
            quotient = quotient + 1

        if negatives == 1:
            quotient = -quotient

        return quotient

    def divide_Positive_Only(self, dividend: int, divisor: int) -> int:
        quotient = 0

        while dividend - divisor >= 0:
            dividend -= divisor
            quotient = quotient + 1

        return quotient
