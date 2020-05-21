# Part 1

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { '(':')', '[':']', '{':'}' }

        for v in s:
            if v in pairs.keys():
                stack.append(v)
            elif stack and v == pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []


# Part 2
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')':'(', ']':'[', '}':'{'}

        for k, v in enumerate(s):
            if v in pairs.values():
                stack.append(v)
            if v in pairs.keys():
                stack_top = stack.pop() if stack else 'NA'
                if pairs[v] != stack_top:
                    return False
        return (len(stack) == 0)

