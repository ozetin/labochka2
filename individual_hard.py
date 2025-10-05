print("Введите цифры трёхзначного числа: ")
a3 = int(input())
a2 = int(input())
a1 = int(input())
print("Введите цифры двузначного числа: ")
b2 = int(input())
b1 = int(input())
s1 = a1 + b1
num1 = s1 % 10
carry1 = s1 // 10
s2 = a2 + b2 + carry1
num2 = s2 % 10
carry2 = s2 // 10
num3 = a3 + carry2
print(num3, num2, num1)