class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a map that tracks element to freq
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        # sort map in reverse based by value
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return_list = []

        # return top k frequent elements
        keys = list(sorted_freq)
        return keys[:k]