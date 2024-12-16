from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        if sorted(freq1.values()) != sorted(freq2.values()):
            return False

        return True
