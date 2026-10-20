from collections import Counter


class Solution:
    def sort_by_frequency(self, array, reverse=True):
        counts = Counter(array)

        return sorted(array, key=lambda x: (counts[x], x), reverse=reverse)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return nums

        sorted_array = self.sort_by_frequency(nums)

        unique_list = list(dict.fromkeys(sorted_array))

        return unique_list[:k]

