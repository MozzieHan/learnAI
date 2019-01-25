

def binary_search(array, val):
    start = 0
    end = len(array) - 1
    mid = int(end/2)
    if len(array) == 0:
        return -1
    if val == array[mid]:
        return mid
    if val < array[mid]:
         return binary_search(array[start: mid], val)
    else:
         return binary_search(array[mid:end-1], val)


def test_binary_search():
    a = list(range(10))

    # 正常值
    assert binary_search(a, 1) == 1
    assert binary_search(a, -1) == -1

    # 异常值
    assert binary_search(None, 1) == -1

    # 边界值
    assert binary_search(a, 0) == 0


if __name__ == '__main__':
    test_binary_search()