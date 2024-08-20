class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        stock = None
        for i in range(len(prices)):
            condition_a = False
            condition_b = False
            if not type(stock) is int:
                if (i < (len(prices) - 1)) and (prices[i] < prices[i + 1]):
                    stock = prices[i]
            else:
                condition_a = (i < (len(prices) - 1)) and (prices[i] > prices[i + 1])
                condition_b = (i == (len(prices) - 1)) and (prices[i] > stock)
                if condition_a or condition_b:
                    total_profit += (prices[i] - stock)
                    stock = None
            print("i = {} | price = {} | stock = {} | total = {} ca = {} | cb = {}".format(i, prices[i], stock, total_profit, condition_a, condition_b))
        return total_profit
        
