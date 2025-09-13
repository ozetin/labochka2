numbers = []
for i in range(4):
    numbers.append(int(input("Enter number\n")))
sum1 = numbers[0] + numbers[1]
sum2 = numbers[2] + numbers[3]
print(round(sum1 / sum2, 2))