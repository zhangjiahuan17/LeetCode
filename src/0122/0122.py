class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        allMoney = 0
        for i in range(0, len(prices)-1):
            if prices[i+1]-prices[i] > 0:
                allMoney = allMoney+(prices[i+1]-prices[i])
        return allMoney


if __name__ == "__main__":
    prices = [1, 2, 3, 4, 5]
    print(Solution().maxProfit(prices))
