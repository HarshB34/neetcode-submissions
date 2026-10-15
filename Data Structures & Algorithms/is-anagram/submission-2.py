class Solution:
    def char_counts(self, s):
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        return counts

    def isAnagram(self, s: str, t: str) -> bool:
       return self.char_counts(s) == self.char_counts(t)


