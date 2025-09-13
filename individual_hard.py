numb2 = [0]
numb3 = []
total = [0,0,0]
for i in input("Enter a two-digit number\n"):
    numb2.append(int(i))
for i in input("Enter a three-digit number\n"):
    numb3.append(int(i))
for i in range(2,-1,-1):
    total[i] += (numb2[i]+numb3[i])%10
    total[i-1] += (numb2[i]+numb3[i])//10
for i in total:
    print(i)