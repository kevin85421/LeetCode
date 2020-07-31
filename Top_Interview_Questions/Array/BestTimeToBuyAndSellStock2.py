def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    buy = []
    sell = []

    # remove duplicates
    curLength = 0
    for i in range(len(prices)):
        if(prices[curLength] != prices[i]):
            curLength = curLength + 1
            prices[curLength] = prices[i]
    prices = prices[:curLength+1]
    
    # max profit
    if len(prices) == 1:
        return profit
    for i in range(len(prices)):
        if i == 0:
            if prices[i] < prices[i+1]:
                buy.append(i)
        elif i == len(prices)-1:
            if prices[i] > prices[i-1]:
                sell.append(i)
        else:
            if (prices[i] < prices[i+1]) and (prices[i] < prices[i-1]):
                buy.append(i)
            elif (prices[i] > prices[i+1]) and (prices[i] > prices[i-1]) and len(buy) > len(sell):
                if(prices[buy[len(buy)-1]] < prices[i]):
                    sell.append(i)

    if len(buy) == 0 or len(sell) == 0:
        return profit
    for i in range(len(buy)):
        profit += prices[sell[i]] - prices[buy[i]]
    return profit