import numpy as np

def merge_sort(sqe):
    if len(sqe) <= 1:
        return sqe

    mid = len(sqe)//2
    left = merge_sort(sqe[:mid])
    right = merge_sort(sqe[mid:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def quick_sort(sqe):
    if len(sqe) <= 1:
        return sqe


if __name__ == '__main__':
    import pprint
    a = [6,4,8,9,10,33,1,89,21,2]
    print(merge_sort(a))
    pprint.pprint(merge_sort(a))

