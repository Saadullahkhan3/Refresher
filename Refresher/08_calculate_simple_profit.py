# Input:
# Enter the principal amount: 1000
# Enter the rate of interest: 5
# Enter the time period in years: 2
# Output:
# Simple Interest: 100.0

def calc_profit(amount: int, rate: int, year: int):
    p = amount/rate * rate 
    return p

print(calc_profit(1000, 5, 20))
    


