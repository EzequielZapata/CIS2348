# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the 
#       pivot, compare the values using two index variables l and h (low and high), 
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, l, h):
    i = (l - 1)
    pivot = user_ids[h]
    
    for j in range(l, h):
        if user_ids[j] <= pivot:
            i = i + 1
            user_ids[i], user_ids[j] = user_ids[j], user_ids[i]
    user_ids[i + 1], user_ids[h] = user_ids[h], user_ids[i + 1]
    return (i + 1)
# TODO: Write the quicksort algorithm that recursively sorts the low and 
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quickSort(user_ids, l, h):
    global num_calls
    num_calls = num_calls + 1
    if l < h:
        p = partition(lst, l, h)
        quickSort(lst, l, p -1)
        num_calls = num_calls + 1
        quickSort(lst, p + 1, h)

lst = []
while True:
    inp = input()
    if inp == "-1":
        break
    else:
        lst.append(inp)
size = len(lst)
quickSort(lst, 0, size - 1)
print(num_calls)
for i in range(size):
    print(lst[i])
