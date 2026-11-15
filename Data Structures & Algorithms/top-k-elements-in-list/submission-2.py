class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a map btwn num and freq
        freq = {} 
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        # create buckets for how many freq's there are
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in freq.items():
            buckets[f].append(n)

        # return top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result