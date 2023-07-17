def Insert(sorted, value):
    i = 0
    while value > sorted[i]:
        i = i + 1
        if i == len(sorted):
            break
    while i < len(sorted):
        temp = sorted[i]
        sorted[i] = value
        value = temp
        i = i + 1
    sorted.append(value)

def InsertionSort(input):
    if len(input) == 0:
        return []
    sorted = []
    sorted.append(input[0])
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted

input_array = [5, 2, 4, 6, 1, 3]
sorted_array = InsertionSort(input_array)
print(sorted_array)