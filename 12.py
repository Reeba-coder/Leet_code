def average(salary):
    min_salary = min(salary)
    max_salary = max(salary)
    total = sum(salary)
    adjusted_total = total - min_salary - max_salary
    return adjusted_total / (len(salary) - 2)
print(average([4000, 3000, 1000, 2000]))  # Output: 2500.0
print(average([1000, 2000, 3000]))        # Output: 2000.0
