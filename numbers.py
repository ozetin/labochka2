numbers = []
for i in range(4):
    print("Enter number")
    numbers.append(int(input()))
sum1 = numbers[0] + numbers[1]
sum2 = numbers[2] + numbers[3]
print(round(sum1/sum2,2))