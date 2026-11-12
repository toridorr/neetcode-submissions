class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for this you are just reassigning variables if you find a lower or higher
        # price so that by the end of it the buy_price is the lowest price in the array 
        # and the max_profit comes from using the highest price in the array. 

        # a constraint is that you must buy before you can sell, so let's just pretend to 
        # buy the first price in the array 
        # and you start with $0.00 
        buy_price = prices[0]
        max_profit = 0 

        # you will go through every element in the array. You want to buy low, sell high. 
        for price in prices:
            # change the buy_price if you encounter a lower price 
            buy_price = min(buy_price, price)
            # change the max_profit if you encounter a higher number 
            max_profit = max(max_profit, price - buy_price) 
        return max_profit 


# Example 1: prices = [10,1,5,6,7,1]
# 1st loop: buy_price = 10, max_profit = 0, price = 10
# buy_price = min(10, 10) = 10
# max_profit = max(0, 10 - 10) = 0
# 2nd loop: buy_price = 10, max_profit = 0, price = 1 
# buy_price = min(10, 1) = 1 
# max_profit = max(0, 1 - 10) = 0 
# 3rd loop: buy_price = 1, max_profit = 0, price = 5 
# buy_price = min(1, 5) = 1 
# max_profit = max(0, 5 - 1) = 4 
# 4th loop: buy_price = 1, max_profit = 4, price = 6 
# buy_price = min(1, 6) = 1 
# max_profit = max(4, 6 - 1) = 5 
# 5th loop: buy_price = 1, max_profit = 5, price = 7 
# buy_price = min(1, 7) = 1
# max_profit = max(5, 7 - 1) = 6 
# 6th loop: buy_price = 1, max_profit = 6, price = 1 
# buy_price = min(1, 1) = 1 
# max_profit = max(6, 1 - 1) = 6 
# returns 6 
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # buy_price = prices[0]
        # max_profit = 0
        # for price in prices: # we need a for loop to move through the array 
        #     buy_price = min(buy_price, price) # this is a more efficient way of writing the if statement
        #     # if price < buy_price: 
        #     #     buy_price = price
        #     max_profit = max(max_profit, price - buy_price) 
        # return max_profit

# 1st example array:
# 1st iteration: price = 10: 10 !< 10 -> if statement doesnt run. The max_profit stays at 0.
# 2nd iteration: price = 1: 1 < 10 -> if statement runs and reassigns buy_price = 1. The max_profit = max(0, 1 - 10) so stays at 0. 
# 3rd iteration: price = 5: 5 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(0, 5 - 1) = 4, max_profit is reassigned to 4.   
# 4th iteration: price = 6: 6 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(4, 6 - 1) = 5, max_profit is reassigned to 5.
# 5th iteration: price = 7: 7 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(5, 7 - 1) = 6, max_profit is reassigned to 6.
# 6th iteration: price = 1: 1 < 1 -> if statement doesn't run, buy_price = 1. The max_profit = max(6, 1 - 1) = 6

        # buy_price = prices[0] # initialize the buy_price as the first element in the price array, if you encounter a lower price you will reassign this variable to it 
        # max_profit = 0 # you are starting with $0.00
    
        # for price in prices:
        #     buy_price = min(buy_price, price)
        #     # if price < buy_price:
        #     #     buy_price = price 
        #     # else:
        #     max_profit = max(max_profit, price - buy_price)
        # return max_profit

# 1st iteration: buy_price = 10, max_profit = 0, price = 10
# 10 !< 10 -> if statement does not run so the else statement runs. 
# max_profit = 0, and price - buy_price = 10 - 10 = 0 so max_profit remains at 0 
# 2nd iteration: buy_price = 10, max_profit = 0, price = 1
# 1 < 10 -> if statement runs and reassigns buy_price = 1 
# 3rd iteration: buy_price = 1, max_profit = 0, price = 5 
# 5 !< 1 -> if statement does not run so the else statement runs.  
# max_profit = 0, and price - buy_price = 5 - 1 = 4. Which is bigger? Max_profit is
# reassigned to 4 
# 4th iteration: buy_price = 1, max_profit = 4, price = 6 
# 6 !< 1 -> if statement does not run so the else statement runs. 
# max_profit = 4, and price - buy_price = 6 - 1 = 5. Which is bigger? Max_profit is 
# reassigned to 5. 
# 5th iteration: buy_price = 1, max_profit = 5, price = 7 
# 7 !< 1 -> if statement does not run so the else statement runs. 
# max_profit = 5, and price - buy_price = 7 - 1 = 6. Which is bigger? Max_profit is 
# reassigned to 6. 
# 6th iteration: buy_price = 1, max_profit = 6, price = 1 
# 1 !< 1 -> if statement does not run so the else statement runs. 
# max_profit = 6, and price - buy_price = 1 - 1 = 0. Which is bigger? Max_profit remains 6 
# That is the end of the for loop so returns max_profit = 6 
























