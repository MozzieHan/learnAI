### 第一章   Python 数据模型

 - namedtuple: 用来构建只有少数属性但没有方法的对象

 - \_\_getitem\_\_ : 通过切片( [] )获取

 - \_\_get\_\_ : 通过点( . )获取

 - for i in x:  这个语句背后用的是 iter(x) , 而这个函数的背后则是 x.\_\_iter\_\_() 方法

 - complex: 复数 

   ```python
   In [1]: complex(1,2)                                              
   Out[1]: (1+2j)
   In [2]: complex("1+2j")                                           
   Out[2]: (1+2j)
   In [3]: complex(1)                                                 
   Out[3]: (1+0j)
   ```

 - \_\_repr\_\_ : repr() , 格式化中的%r  和  .format() 函数 都会调用此方法

 - \_\_str\_\_ : str() 和 print()  时调用, 当没有实现 \_\_str\_\_ 时 解释器会调用 \_\_repr\_\_ 方法

 - \_\_bool\_\_ : bool() 函数调用, 如果不存在\_\_bool\_\_ 方法, 调用 \_\_len\_\_ 方法,  若都没实现, 默认返回True

 - 真值表

   | --      | --                                         |
   | ------- | ------------------------------------------ |
   | x or y  | if *x* is false, then *y*, else *x*        |
   | x and y | if *x* is false, then *x*, else *y*        |
   | not x   | if *x* is false, then `True`, else `False` |

### 第二章  序列构成的数组

 - 列表或元组的方法和属性(那些由object类支持的方法没有列出来)

   | 方 法 | 列 表 | 元 组 | 示例 |
   | -- | -- | -- | -- |
   | s.\_\_add\_\_(s2) | •    | •    | s + s2 ,拼接 |
   | s.\_\_iadd\_\_(s2) | •    |      | s += s2 ,就地拼接 |
   | s.append(e) | •    |      | 在尾部添加一个新元素 |
   | s.clear() | •    |      | 删除所有元素 |
   | s.\_\_contains\_\_(e) | • | • | s 是否包含 e |
   | s.copy() | • | | 列表的浅复制 |
   | s.count(e) | • | • | e 在 s 中出现的次数 |
   | s.\_\_delitem\_\_(p) | • |  | 把位于 p 的元素删除 |
   | s.extend(it) | • |  | 把可迭代对象 it 追加给 s |
   | s.\_\_getitem\_\_(p) | • | • | s[p] ,获取位置 p 的元素|
   | s.\_\_getnewargs\_\_() |  | • | 在 pickle 中支持更加优化的序列化 |
   | s.index(e) | • | • | 在 s 中找到元素 e 第一次出现的位置|
   | s.insert(p, e) | • | | 在位置 p 之前插入元素e |
   | s.\_\_iter\_\_() | • | • | 获取 s 的迭代器 |
   | s.\_\_len\_\_() | • | • | len(s) ,元素的数量 |
   | s.\_\_mul\_\_(n) | • | • |  s * n , n |
   | s.\_\_imul\_\_(n) | • |  | s \*= n ,就地重复拼接|
   | s.\_\_rmul\_\_(n) | • | • | n * s ,反向拼接 * |
   | s.pop([p]) | • | | 删除最后或者是(可选的)位于 p 的元素,并返回它的值 |
   | s.remove(e) | • | | 删除 s 中的第一次出现的 e |
   | s.reverse() | • | | 就地把 s 的元素倒序排列|
   | s.\_\_reversed\_\_()| • |  | 返回 s 的倒序迭代器|
   | s.\_\_setitem\_\_(p,e) | • |  | s[p] = e ,把元素 e 放在位置p,替代已经在那个位置的元素|
   | s.sort([key], [reverse]) | • |  | 就地对 s 中的元素进行排序,可选的参数有键( key )和是否倒序( reverse ) |

 - bisect.bisect(haystack, needle)  二分查找, haystack: 有序序列, needle: 插入这个位置后还能保持升序

 - bisect.insort(haystack, needle)  二分查找方式插入值.

 - 数组: 如果我们需要一个只包含数字的列表,那么 array.array 比 list 更高效

 - 列表和数组的属性和方法(不包含过期的数组方法以及那些由对象实现的方法)

   |                         | 列表 | 数组 |                                                              |
   | ----------------------- | ---- | ---- | ------------------------------------------------------------ |
   | s.\__add__(s2)          | •    | •    | s + s2, 拼接                                                 |
   | s.\__iadd__(s2)         | •    | •    | s += s2, 就地拼接                                            |
   | s.append(e)             | •    | •    | 在尾部添加一个元素                                           |
   | s.byteswap              | •    |      | 翻转数组内每个元素的字节序列,转换字节序                      |
   | s.clear()               | •    | •    | 删除所有元素                                                 |
   | s.\__contains__(e)      | •    | •    | s是否含有e                                                   |
   | s.copy()                | •    |      | 对列表浅复制                                                 |
   | s.\__copy__()           |      | •    | 对 copy.copy 的支持                                          |
   | s.count(e)              | •    | •    | s中 e 出现的次数                                             |
   | s.\__deepcopy__()       |      | •    | 对 copy.deepcopy 的支持                                      |
   | s.\__delitem__(p)       | •    | •    | 删除位置 p 的元素                                            |
   | s.extend(it)            | •    | •    | 将可迭代对象 it 里的元素添加到尾部                           |
   | s.frombytes(b)          |      | •    | 将压缩成机器值的字节序列读出来添加到尾部                     |
   | s.fromfile(f, n)        |      | •    | 将二进制文件 f 内含有机器值读出来添加到尾部,最多添加 n 项    |
   | s.fromlist(l)           |      | •    | 将列表里的元素添加到尾部,如果其中任何一个元素导致了 TypeError 异常,那么所有的添加都会取消 |
   | s.\__getitem__(p)       | •    | •    | s[p] ,读取位置 p的元素                                       |
   | s.index(e)              | •    | •    | 找到 e 在序列中第一次出现的位置                              |
   | s.insert(p, e)          | •    | •    | 在位于 p 的元素之前插入元素 e                                |
   | s.itemsize              |      | •    | 数组中每个元素的长度是几个字节                               |
   | s.\__iter__()           | •    | •    | 返回迭代器                                                   |
   | s.\__len__()            | •    | •    | len(s) ,序列的长度                                           |
   | s.\__mul__(n)           | •    | •    | s * n ,重复拼接                                              |
   | s.\__imul__(n)          | •    | •    | s *= n ,就地重复拼接                                         |
   | s.\__rmul__(n)          | •    | •    | n * s ,反向重复拼接                                          |
   | s.pop([p])              | •    | •    | 删除位于 p 的值并返回这个值, p 的默认值是最后一个元素的位置  |
   | s.remove(e)             | •    | •    | 删除序列里第一次出现的 e 元素                                |
   | s.reverse()             | •    | •    | 就地调转序列中元素的位置                                     |
   | s.\__reversed__()       | •    |      | 返回一个从尾部开始扫描元素的迭代器                           |
   | s.\__setitem__(p, e)    | •    | •    | s[p] = e ,把位于 p<br/>位置的元素替换成 e                    |
   | s.sort([key], [revers]) | •    |      | 就地排序序列,可选参数有 key 和 reverse                       |
   | s.tobytes()             |      | •    | 把所有元素的机器值用 bytes 对象的形式返回                    |
   | s.tofile(f)             |      | •    | 把所有元素以机器值的形式写入一个文件                         |
   | s.tolist()              |      | •    | 把数组转换成列表,列表里的元素类型是数字对象                  |
   | s.typecode              |      | •    | 返回只有一个字符的字符串,代表数组元素在 C 语言中的类型       |

 - memoryview:  是一个内置类,它能让用户在不复制内容的情况下操作同一个数组的不同切片

   ```python
   >>> numbers = array.array('h', [-2, -1, 0, 1, 2])
   >>> memv = memoryview(numbers) 
   >>> len(memv)
   5
   >>> memv[0] 
   -2
   >>> memv_oct = memv.cast('B') 
   >>> memv_oct.tolist() 
   [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
   >>> memv_oct[5] = 4 
   >>> numbers
   array('h', [-2, -1, 1024, 1, 2])
   ```

 - deque : 双向队列

   ```python
   >>> from collections import deque
   >>> dq = deque(range(10), maxlen=10) 
   >>> dq
   deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
   >>> dq.rotate(3) 
   >>> dq
   deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
   >>> # 队列的旋转操作接受一个参数 n,当 n > 0 时,队列的最右边的 n 个元素会被移动到队列的左边。当 n < 0 时,最左边的 n 个元素会被移动到右边。
   >>> dq.rotate(-4)
   >>> dq
   deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
   >>> dq.appendleft(-1) 
   >>> dq
   deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
   >>> dq.extend([11, 22, 33]) 
   >>> dq
   deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
   >>> dq.extendleft([10, 20, 30, 40]) 
   >>> dq
   deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
   ```

 - 

 - 