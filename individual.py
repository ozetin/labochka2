assortment = ["sweets","cookies","apples"]
price = []
total = 0
for i in range(3):
    price.append(int(input(f"Enter the price of {assortment[i]}")))
for i in range(3):
    total += int(input(f"How many {assortment[i]} did you buy?")) * price[i]
print(f"Your total is: {total}")
