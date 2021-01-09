class LC0067_Add_Binary:
    def addBinary(self, a: str, b: str) -> str:

        # Assume a is longer
        if len(b) > len(a):
            return self.addBinary(b, a)

        carry = 0
        res = [None] * len(a)
        bPos = len(b) - 1

        for aPos in range(len(a)-1, -1, -1):

            if a[aPos] == '1':
                carry += 1

            if bPos >= 0:
                if b[bPos] == '1':
                    carry += 1
                bPos -= 1

            res[aPos] = '0' if carry % 2 == 0 else '1'
            carry = 1 if carry > 1 else 0

        ret = '1' + ''.join(res) if carry == 1 else ''.join(res)

        return ret