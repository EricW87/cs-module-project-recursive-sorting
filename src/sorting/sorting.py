# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    lenA = len(arrA)
    lenB = len(arrB)
    elements = lenA + lenB
    merged_arr = [0] * elements
    print("merge arrA, arrB, elements, merged_arr: " + str(arrA) + str(arrB) +  ' ' + str(elements) + str(merged_arr))
    # Your code here
    index = 0
    while lenA > 0 or lenB > 0:
        if lenA > 0 and lenB > 0:
            if arrB[0] > arrA[0]:
                merged_arr[index] = arrA.pop(0)
            else:
                merged_arr[index] = arrB.pop(0)
        elif lenA > 0:
            merged_arr[index] = arrA.pop(0)
        else:
            merged_arr[index] = arrB.pop(0)

        index += 1
        lenA = len(arrA)
        lenB = len(arrB)
        print("lenA, lenB, merged_arr: " + str(lenA) + str(lenB) + str(merged_arr))

    print("merged_arr: " + str(merged_arr))
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        arrL = len(arr) - 1
        middle = arrL // 2
        lhs = []
        rhs = []

        for x in range(len(arr)):
            if x <= middle:
                lhs.append(arr[x])
            else:
                rhs.append(arr[x])
        print(arr, lhs, rhs)
        lhs = merge_sort(lhs)
        rhs = merge_sort(rhs)
        arr = merge(lhs, rhs)

    print("merge_sort returned arr: " + str(arr))
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

