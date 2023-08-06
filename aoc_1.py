with open('input_1.txt') as f:
    arr = f.readlines()

sum = 0
arr1 = []

for i in range(len(arr)):
    if arr[i] != '\n':
        sum = sum + int(arr[i][0:-1])
        
    elif arr[i] == '\n':
        arr1.append(sum)
        sum = 0


tmax = 0

for j in range(3):
    max = arr1[0]
    for i in range(len(arr1)):
        if max <= int(arr1[i]):
            max = int(arr1[i])
        else:
            continue
    tmax = tmax + max
    arr1.remove(max)


print(tmax)

