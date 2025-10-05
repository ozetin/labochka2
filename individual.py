sweets = int(input("Enter the price of sweets: "))
cookies = int(input("Enter the price of cookies: "))
apples = int(input("Enter the price of apples: "))
sweets_amount = int(input("How many sweets did you buy? "))
cookies_amount = int(input("How many cookies did you buy? "))
apples_amount = int(input("How many apples? "))
total = 0
total += sweets * sweets_amount
total += cookies * cookies_amount
total += apples * apples_amount
print(f"Your total is: {total}")
