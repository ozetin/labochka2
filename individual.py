assortment = ["sweets","cookies","apples"]
price = []
sum = 0
for i in range(3):
    print(f"Enter the price of {assortment[i]}")
    price.append(int(input()))
for i in range(3):
    print(f"How many {assortment[i]} did you buy?")
    sum += int(input()) * price[i]
print(f"Your total is: {sum}")
