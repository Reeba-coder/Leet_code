def maxProfit(prices):
    buy=prices[0]
    sell=0
    profit=sell-buy
    for i in prices:
        if i <buy:
            buy=i
        else:
            profit=max(profit, i  - buy)
    return profit
print(maxProfit([7,1,5,3,6,4]))