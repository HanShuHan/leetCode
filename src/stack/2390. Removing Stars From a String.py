class Solution(object):
    def removeStars(self, s):
        stack = []

        for c in s:
            if c == '*' and stack:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)