# Roman strings to integer
def romanTOint(s):
    roam= {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total =0
    first_value=0
    for char in reversed(s):
        current_value=roam[char]
        if current_value< first_value:
            total-=current_value
        else:
            total+=current_value
        first_value=current_value
    return total
roman = "MCMXC"
result = romanTOint(roman)
print(f"Roman numeral {roman} = {result}")
