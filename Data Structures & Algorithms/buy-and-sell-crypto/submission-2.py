class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = [0]

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit.append(profit)

        return max(max_profit)