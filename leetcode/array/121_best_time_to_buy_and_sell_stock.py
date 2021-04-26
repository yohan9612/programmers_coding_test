class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute Force
        """
        max_price = 0
        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price

        """
        My solving
        """
        max_price = 0
        min_price = prices[0]

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_price:
                max_price = prices[i] - min_price
        return max_price

        """
        O(N) solving
        """
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
