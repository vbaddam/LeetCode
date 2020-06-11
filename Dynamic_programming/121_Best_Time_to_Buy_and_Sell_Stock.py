class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = float('inf')
        for i in range(0,len(prices)):
            if l > prices[i]:
                l = prices[i]
            else:
                p = max(prices[i] - l, p)
        return(p)
