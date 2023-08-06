with open('input_2.txt') as f:
    arr = f.readlines()

x=[i for a,i in enumerate(arr) ]
print(x)

n = len(arr)

point = 0

print(n)

for i in range(0,n):
    if (arr[i][0] == 'A' and arr[i][2] == 'Y') or (arr[i][0] == 'B' and arr[i][2] == 'Z') or (arr[i][0] == 'C' and arr[i][2] == 'X'):
            point = point + 6 
            """
            if arr[i][2] == 'X':
            point = point + 1
            if arr[i][2] == 'Y':
            point = point + 2
            """
            if arr[i][2] == 'Z':
                point = point + 1
    if (arr[i][0] == 'A' and arr[i][2] == 'X') or (arr[i][0] == 'B' and arr[i][2] == 'Y') or (arr[i][0] == 'C' and arr[i][2] == 'Z'):
        point = point + 3 
        """
        if arr[i][2] == 'X':
        point = point + 1
        """
        if arr[i][2] == 'Y':
            point = point + 1
            """
            if arr[i][2] == 'Z':
            point = point + 3
            """
    elif (arr[i][0] == 'A'and (arr[i][2] == 'X' or arr[i][2] == 'Z')) or  (arr[i][0] == 'B'and (arr[i][2] == 'X' or arr[i][2] == 'Y')) or (arr[i][0] == 'C'and (arr[i][2] == 'Y' or arr[i][2] == 'Z')):
        if arr[i][2] == 'X':
            point = point + 1
            """
            if arr[i][2] == 'Y':
            point = point + 2
            if arr[i][2] == 'Z':
            point = point + 3
            """
print(point)
        


