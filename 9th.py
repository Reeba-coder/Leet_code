def maximumwealth(accounts):
    max_wealth=0
    for customer in accounts:
        wealth=sum(customer)
        max_wealth=max(max_wealth, wealth)
    return max_wealth
accounts = [[1, 4], [5, 7], [7, 4]]
print(accounts)
print(maximumwealth(accounts))