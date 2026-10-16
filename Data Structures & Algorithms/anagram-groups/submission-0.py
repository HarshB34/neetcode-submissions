class Solution:
    def char_counts(self, s):
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        return counts

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for w in strs:
            key = frozenset(self.char_counts(w).items())
            if key not in groups:
                groups[key] = []
            groups[key].append(w)
            

        result = list(groups.values())
        return result
    



                
                


                