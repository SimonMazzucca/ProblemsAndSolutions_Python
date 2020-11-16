class LC0020_Valid_Parentheses:

    def isValid(self, s: str) -> bool:
        stack = []
        par = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for curr in s:
            if curr in par.keys():
                stack.append(curr)

            else:
                if len(stack) == 0:
                    return False

                # see if we are popping an open parens
                close = par[stack.pop()]
                if curr != close:
                    return False

        return len(stack) == 0
