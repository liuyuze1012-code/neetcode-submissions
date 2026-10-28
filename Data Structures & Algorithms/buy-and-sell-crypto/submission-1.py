class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        l, r = 0 ,1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            elif prices[r] <= prices[l]:
                l = r
            r += 1

        return max_profit




# 10 1 5 6 7 1
#            r
#    l