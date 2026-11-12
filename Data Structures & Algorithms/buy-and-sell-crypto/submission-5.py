class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0 

        for price in prices:
            buy_price = min(buy_price, price)
            max_profit = max(max_profit, price - buy_price)

        return max_profit 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # MIDTERM REVIEW 
        # window_sum = sum(nums[:3])
        # max_sum = window_sum 

        # for num in range(k, len(nums)):
        #     window_sum = window_sum + nums[num] - nums[num - k]
        #     max_sum = max(max_sum, window_sum)

        # return max_sum 



        # Example: nums = = [10,1,5,6,7,1], k = 3 
        # 1st loop: 
        # window_sum = 10 + 1 + 5 = 16 
        # max_sum = 16 
        # num = index 3 
        # window_sum = window_sum + nums[3] - nums[3 - 3] = window_sum + nums[3] - nums[0] = 16 + 6 - 10 = 12
        # max_sum = max(16, 12) = 16 
        # 2nd loop: num = index 4 
        # window_sum = 12 + 7 - nums[4 - 3] = 12 + 7 - 1 = 18 
        # max_sum = max(16, 18) = 18 
        # 3rd loop: num = index 5 
        # window_sum = 18 + 1 - nums[5 - 3] = 18 + 1 - nums[2] = 18 + 1 - nums[2] = 18 + 1 - 5 = 14 
        # max_sum = max(18, 14) = 18 < return 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Maximum Sum Subarray of Size K  
        # window_sum = sum(nums[:3]) 
        # max_sum = window_sum 

        # for end in range(k, len(nums)):
        #     window_sum = window_sum - nums[end - k] + nums[end]
        #     max_sum = max(max_sum, window_sum)
        
        # return max_sum 
    
    
    
    # MIDTERM REVIEW 
        # buy = prices[0]
        # max_profit = 0

        # for price in prices:
        #     buy = min(buy, price) #somehow missed putting 'min' here 
        #     max_profit = max(max_profit, price - buy)
        
        # return max_profit 

        # Example: prices = [7, 1, 5, 3, 6, 4] 
        # 1st loop: price = 7, buy = 7, max_profit = 0  
        # buy = min(7, 7) = 7 
        # max_profit = max(0, 7 - 7) = 0 
        # 2nd loop: price = 1, buy = 7, max_profit = 0 
        # buy = min(7, 1) = 1 
        # max_profit = max(0, 1 - 7) = 0
        # 3rd loop: price = 5, buy = 1, max_profit = 0 
        # buy = min(1, 5) = 1 
        # max_profit = max(0, 5 - 1) = 4 
        # 4th loop: price = 3, buy = 1, max_profit = 4 
        # buy = min(1, 3) = 1
        # max_profit = max(4, 3 - 1) = 4 
        # 5th loop: price = 6, buy = 1, max_profit = 4 
        # buy = min(1, 6) = 1 
        # max_profit = max(4, 6 - 1) = 5 
        # 6th loop: price = 4, buy = 1, max_profit = 5 
        # buy = min(1, 4) = 1 
        # max_profit = max(5, 4 - 1) = 5 

        # return 5 

        # Complexity:
        # Time = O(n) because a for loop
        # Space = O(1) because we aren't creating anything new, just dealing with variables 
    




    # ITERATION - INITIAL ATTEMPT
        # for this you are just reassigning variables if you find a lower or higher
        # price such that buy_price is minimized and max_profit is maximized given the
        # rule that you must buy before you can sell. Buy low, sell high.

        # buy_price = prices[0]
        # max_profit = 0 
 
        # for price in prices: 
        #     buy_price = min(buy_price, price) # yay! finally used min()
        #     max_profit = max(max_profit, price - buy_price) 
        # return max_profit 


    # ITERATION (LONGER SOLUTION) 

        # buy_price = prices[0] # initialize the buy_price as the first element in the price array, if you encounter a lower price you will reassign this variable to it 
        # max_profit = 0 
    
        # for price in prices:
        #     if price < buy_price: # We can use min() here instead, see above
        #         buy_price = price 
        #     max_profit = max(max_profit, price - buy_price) # don't need to have 'else' here
                
        # return max_profit



















