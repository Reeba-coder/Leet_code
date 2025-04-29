def count_odd(low, high):
    return(high-low )//2 +(1 if low%2!=0and high%2!=0 else 0)
print (count_odd(3,7))
print(count_odd(4,8))
print(count_odd(1,10))
