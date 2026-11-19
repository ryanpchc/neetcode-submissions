class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left: sell, right: buy
        maxProfit = 0

        # sliding window
        while r < len(prices):
            # is this a profit? ideally, right ptr > left ptr
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            # if not profit, update left ptr
            else:
                l = r
            r += 1

        return maxProfit