class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a map that tracks element to freq
        freq = {}

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        # create separate bucket for every possible freq
        buckets = [[] for _ in range(len(nums) + 1)]

        for number, count in freq.items():
            buckets[count].append(number)

        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for number in buckets[count]:
                result.append(number)

            if len(result) == k:
                return result