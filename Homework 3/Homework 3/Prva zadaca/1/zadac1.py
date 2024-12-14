import random


niza_1 = [random.randint(1, 100) for _ in range(10)]
niza_2 = [random.randint(1, 100) for _ in range(10)]


result = []
count_1 = 0
count_2 = 0

for i in range(10):
    if niza_1[i] > niza_2[i]:
        result.append(niza_1[i])
        count_1 += 1
    elif niza_2[i] > niza_1[i]:
        result.append(niza_2[i])
        count_2 += 1
    else:
        result.append(0)


print("niza_1:", niza_1)
print("niza_2:", niza_2)
print("result:", result)


if count_1 > count_2:
    print("Повеќе елементи има од niza_1")
elif count_2 > count_1:
    print("Повеќе елементи има од niza_2")
else:
    print("Има еднаков број на елементи од двете низи")
