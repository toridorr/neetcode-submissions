class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for price in prices: # we need a for loop to move through the array 
            buy_price = min(buy_price, price) # this is a more efficient way of writing the if statement
            # if price < buy_price: 
            #     buy_price = price
            max_profit = max(max_profit, price - buy_price) 
        return max_profit

# 1st example array:
# 1st iteration: price = 10: 10 !< 10 -> if statement doesnt run. The max_profit stays at 0.
# 2nd iteration: price = 1: 1 < 10 -> if statement runs and reassigns buy_price = 1. The max_profit = max(0, 1 - 10) so stays at 0. 
# 3rd iteration: price = 5: 5 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(0, 5 - 1) = 4, max_profit is reassigned to 4.   
# 4th iteration: price = 6: 6 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(4, 6 - 1) = 5, max_profit is reassigned to 5.
# 5th iteration: price = 7: 7 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(5, 7 - 1) = 6, max_profit is reassigned to 6.
# 6th iteration: price = 1: 1 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(6, 1 - 1) = 6



        