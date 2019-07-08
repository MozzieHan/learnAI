

# 冒泡
def bubble_sort(values:list)->list:
    length = len(values)
    for i in range(length-1):
        for j in range(length-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]


# 选择
def select_sort(values):
    length = len(values)
    for i in range(length-1):
        _min=i
        for j in range(i, length):
            if values[j]< values[_min]:
                _min = j
        values[i], values[_min] = values[_min], values[i]


# 插入
def insert_sort(values):
    length = len(values)
    for i in range(1, length):
        for j in range(i):
            if values[i] < values[j]:
                tmp_val = values[i] 
                values.pop(i)
                values.insert(j, tmp_val)

# 快排
# def quick_sort(values, first, last):

count = 0
import random

def quick_sort(lists, start, end):
    global count
    count += 1
    if start >= end:
        return lists
    low = start
    high = end
    rand = random.randint(start, end)
    lists[low], lists[rand] = lists[rand], lists[low]
    mid = lists[low]
    while low < high:
        while low < high and lists[high] > mid:
            high -= 1
        lists[low] = lists[high]
        while low < high and lists[low] < mid:
            low += 1
        lists[high] = lists[low]
    lists[low] = mid
    quick_sort(lists, start, low-1)
    quick_sort(lists, low+1, end)


if __name__ == "__main__":
    test_values = [3,29,0,11,4,32,88,2,132,9]
    # select_sort(test_values)
    # insert_sort(test_values)
    quick_sort(test_values, 0, 9)
    print(test_values)
    print(count)

