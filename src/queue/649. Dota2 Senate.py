from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        cycle = len(senate)
        radiants = deque()
        dires = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                radiants.append(i)
            else:
                dires.append(i)

        while radiants and dires:
            r = radiants.popleft()
            d = dires.popleft()

            if r < d:
                radiants.append(r + cycle)
            else:
                dires.append(d + cycle)

        return 'Radiant' if radiants else 'Dire'
