




def max_profit(prices):

    min_so_far = prices[0]
    maximum = 0
    for i in range(1,len(prices)):
        price = prices[i]
        maximum = max(maximum,price - min_so_far)

        min_so_far =min(min_so_far,price)
    
    return maximum


def max_profit_two_trades(prices):


    best_to_here = [0] * len(prices)
    min_so_far = prices[0]
    maximum = 0 
    for i in range(1,len(prices)):
        price = prices[i]
        
        maximum = max(maximum,price - min_so_far)
        best_to_here[i] = maximum

        min_so_far = min(min_so_far,price)


    best_from_here = [0] * len(prices)
    max_so_far = prices[-1]
    maximum = 0
    for i in range(len(prices) - 2,-1,-1):
        price = prices[i]

        maximum = max(maximum,max_so_far - price)

        best_from_here[i] = maximum

        max_so_far = max(max_so_far,price)

    

    max_profit = 0

    for i in range(0,len(maximum) - 1):
        max_profit = max(max_profit,best_to_here[i] + best_from_here[i + 1])

    
    return max(max_profit,best_to_here[-1])


