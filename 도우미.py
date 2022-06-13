# a = open("C:\\Users\\Jun\\Downloads\\random.txt", 'r')

# num = a.readline().split()
num = [75, 56, 38, 98, 62, 3, 81, 17, 52, 43]
# print(num)

num_len = 0
for x in num:
    if len(x) > num_len:
        num_len = len(x)

for x in range(len(num)):
    if len(num[x]) == num_len:
        continue

    else:
        num[x] = '0' * (num_len - len(num[x]))

while True:
    radix_sort = [[] for _ in range(10)]
    num_len -= 1

    if num_len < 0:
        break

    for x in num:
        radix_sort[int([num_len])].append(x)

    new_num = []

    for x in radix_sort:
        for y in x:
            new_num.append(y)

    num = new_num
result = []
for x in num:
    result.append(int(x))

print(num)
print(result)

