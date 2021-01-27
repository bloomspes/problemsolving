# 두 수의 합이 7이 되는 각 구간의 갯수 (순서쌍) 구하기

data = [1, 2, 4, 7, 3, 5, 6, 2, 1, 1, 3, 4, 5, 3, 2, 2]

count = 0
sum = 0
left, right = 0, 0

for start in range(len(data)):
    while sum < 7 and right < len(data):
        sum += data[right]
        right += 1
    if sum == 7:
        count += 1
    sum -= data[left]

print(count)
