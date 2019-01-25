#### 创建array

- np.array([1,2,3,4])
- np.arange(4).reshap(2,2)
- np.random.random((2,2))
- np.zeros((3,2))
- np.empty((2,4))

#### array 属性

- a.shape   形状
- a.ndim    深度
- a.size    大小
- a.dtype   类型

#### 计算

- 最大, 最小, 求和, 品均
    - np.sum(a, axis=1)  a的每行求和
    - np.max(a, axis=0)  a的每列的最大值
    - np.min(a)          a的最小值
    - np.argmax(a)       a最大值的位置
    - np.argmin(a)
    - np.mean(a)  np.average(a)  a.mean()   a的平均值
    - np.cumsum(a)       累加和
    - np.nonzero(a)      a中非0的行号和列号
    - np.sort(a)         a 中每行的排序
    - a.T   np.transpose(a)     a的转置
    - np.clip(a, 3, 5)   a中小于3的变为3, 大于5的变为5
    
- 数学计算
    - a.dot(b)    np.dot(a, b)
    - a * b       np.multiply(a, b)
    - a / b       np.divide(a, b)
    - a + b       np.add(a, b)
    - a - b       np.subtract(a, b)
    
#### numpy 索引

```python
import numpy as np

a = np.arange(3, 15)
print(a)
print(a[3])
# >>> [ 3  4  5  6  7  8  9 10 11 12 13 14]
# >>> 6

a = a.reshape(3, 4)
print(a)
print(a[2])    # a[2, :]
print(a[:, 1])
print(a[1, 1])  # a[1][1]
print(a[1, 1:3])
print(a.flatten())  # a.flat 返回一个迭代器
# >>> [[ 3  4  5  6]
#      [ 7  8  9 10]
#      [11 12 13 14]]
# >>> [11 12 13 14]
# >>> [ 4  8 12]
# >>> 8
# >>> [8 9]
# >>> [ 3  4  5  6  7  8  9 10 11 12 13 14]
```

#### numpy 合并
```python
import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])

print(np.vstack((a, b)))
print(np.hstack((a, b)))
# >>> [[1 1 1]
#      [2 2 2]]
# >>> [1 1 1 2 2 2]

a_1 = a.reshape(3,1)
b_1 = b.reshape(3,1)
print(np.vstack((a_1, b_1)))
print(np.hstack((a_1, b_1)))
# >>> [[1]
#      [1]
#      [1]
#      [2]
#      [2]
#      [2]]
# >>> [[1 2]
#      [1 2]
#      [1 2]]

print(a[np.newaxis, :])
print(b[:, np.newaxis])
# >>> [[1 1 1]]
# >>> [[2]
#      [2]
#      [2]]

print(np.concatenate((a_1, a_1, a_1), axis=0))
print(np.concatenate((a_1, a_1, a_1), axis=1))
# >>> [[1 1 1]
#      [1 1 1]
#      [1 1 1]]
# >>> [[1 1 1 1 1 1 1 1 1]]
```

#### numpy分割

```python
import numpy as np
a = np.arange(12).reshape(3, 4)
print(a)
# >>> [[ 0  1  2  3]
#      [ 4  5  6  7]
#      [ 8  9 10 11]]

print(np.split(a, 2, axis=1))
print(np.split(a, 3, axis=0))
# >>> [array([[0, 1],
#      [4, 5],
#      [8, 9]]), array([[ 2,  3],
#      [ 6,  7],
#      [10, 11]])]
# >>> [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.array_split(a,3, axis=1))
# >>>[array([[0, 1],
#           [4, 5],
#           [8, 9]]), array([[ 2],
#           [ 6],
#           [10]]), array([[ 3],
#           [ 7],
#           [11]])]

print(np.vsplit(a, 3))
print(np.hsplit(a, 2))
# >>> [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
# >>> [array([[0, 1],
#             [4, 5],
#             [8, 9]]), array([[ 2,  3],
#             [ 6,  7],
```

