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
   >>d.setdefault(k,
   [default])
   d.__setitem__(k,
   v)
   d.update(m,
   [**kargs])
   d.values()
   • • •
   • • •
   • • •
   • • •
   若字典里有键k,则把它对应的值
   设置为 default ,然后返回这个
   值;若无,则让 d[k] =
   default ,然后返回 default
   实现 d[k] = v 操作,把 k 对应的
   值设为v
   可以是映射或者键值对迭代
   器,用来更新 d 里对应的条目
   m
   返回字典里的所有值> dq
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



### 第三章 字典和集合

 - **可散列数据类型**:  如果一个对象是可散列的,那么在这个对象的生命周期中,它的散列值是不变的,而且这个对象需要实现 \_\_hash\_\_() 方法。另外可散列对象还要有 \_\_qe\_\_() 方法,这样才能跟其他键做比较。如果两个可散列对象是相等的,那么它们的散列值一定是一样的......

 - 原子不可变数据类型(str、bytes 和数值类型)都是可散列类型,frozenset 也是可散列的,因为根据其定义,frozenset里只能容纳可散列类型。元组的话,只有当一个元组包含的所有元素都是可散列类型的情况下,它才是可散列的。

 - 一般来讲用户自定义的类型的对象都是可散列的,散列值就是它们的 id() 函数的返回值,所以所有这些对象在比较的时候都是不相等的。如果一个对象实现了 \__eq__ 方法,并且在方法中用到了这个对象的内部状态的话,那么只有当所有这些内部状态都是不可变的情况下,这个对象才是可散列的。

 - dict、collections.defaultdict 和 collections.OrderedDict

   |                           | dict | defaultdict | OrderedDict |                                                              |
   | ------------------------- | ---- | ----------- | ----------- | ------------------------------------------------------------ |
   | d.clear()                 | •    | •           | •           | 移除所有元素                                                 |
   | d.\__contains__(k)        | •    | •           | •           | 检查 k 是否在 d 中                                           |
   | d.copy()                  | •    | •           | •           | 浅复制                                                       |
   | d.\__copy__()             |      | •           |             | 用于支持 copy.copy                                           |
   | d.default_factory         |      | •           |             | 在 \__missing__ 函数中被调用的函数,用以给未找到的元素设置e值, <br/>是一个可调用对象(callable),它的值在 defaultdict 初始化的时候由用户设定 |
   | d.\__delitem__(k)         | •    | •           | •           | del d[k] ,移除键为 k                                         |
   | d.fromkeys(it,[initial])  | •    | •           | •           | 将迭代器 it 里的元素设置为映射里的键,如果有 initial 参数,就把它作为这些键对应的值(默认是 None ) |
   | d.get(k,[default])        | •    | •           | •           | 返回键 k 对应的值,如果字典里没有键 k ,则返回 None 或者default |
   | d.\__getitem__(k)         | •    | •           | •           | 让字典 d 能用 d[k] 的形式返回键k 对应的值                    |
   | d.items()                 | •    | •           | •           | 返回 d 里所有的键值对                                        |
   | d.\__iter__()             | •    | •           | •           | 获取键的迭代器                                               |
   | d.keys()                  | •    | •           | •           | 获取所有的键                                                 |
   | d.\__len__()              | •    | •           | •           | 可以用 len(d) 的形式得到字典里键值对的数量                   |
   | d.\__missing__(k)         |      | •           |             | 当 \__getitem__ 找不到对应键的时候,这个方法会被调用          |
   | d.move_to_end(k,[last])   |      |             | •           | 把键为 k 的元素移动到最靠前或者最靠后的位置( last 的默认值是 True ) |
   | d.pop(k, [defaul])        | •    | •           | •           | 返回键 k 所对应的值,然后移除这个键值对。如果没有这个键,返回 None 或者 defaul |
   | d.popitem()               | •    | •           | •           | 随机返回一个键值对并从字典里移除它, OrderedDict 移除的是最后一个元素, 还可指定 last=False 来移除地一个元素 |
   | d.\__reversed__()         |      |             | •           | 返回倒序键的迭代器                                           |
   | d.setdefault(k,[default]) | •    | •           | •           | 若字典里有键k, 返回对应的值. 若无, 则让 d[k] =default ,然后返回 default |
   | d.\__setitem__(k,v)       | •    | •           | •           | 实现 d[k] = v 操作,把 k 对应的值设为v                        |
   | d.update(m,[**kargs])     | •    | •           | •           | m 可以是映射或者键值对迭代器,用来更新 d 里对应的条目         |
   | d.values()                | •    | •           | •           | 返回字典里的所有值                                           |

 - \__missing__:  obj[ ]  (\_\_getitem\_\_)  找不的对应键时, 会调用这个方法

 - \_\_missing__ 方法只会被 \_\_getitem\_\_ 调用(比如在表达式 d[k] 中)。提供 \_\_missing\_\_ 方法对get 或者\_\_contains\_\_(in 运算符会用到这个方法)这些方法的使用没有影响。defaultdict 中的 default_factory 只对 \_\_getitem\_\_ 有作用的原因

 - 自定义dict

   ```python
   class StrKeyDict0(dict):
   	def __missing__(self, key):
   		if isinstance(key, str): 
   			raise KeyError(key)
   	return self[str(key)] 
   
   	def get(self, key, default=None):
   		try:
   			return self[key] 
   		except KeyError:
   			return default 
   	def __contains__(self, key):
   		return key in self.keys() or str(key) in self.keys()
   ```

 - colllections.UserDict:  这个类其实就是把标准 dict 用纯 Python 又实现了一遍。跟 OrderedDict、ChainMap 和 Counter 这些开箱即用的类型不同,UserDict 是让用户继承写子类的。

   ```python	
   import collections
   class StrKeyDict(collections.UserDict):
   	def __missing__(self, key): 
   		if isinstance(key, str):
   			raise KeyError(key)
   		return self[str(key)]
   	def __contains__(self, key):
   		return str(key) in self.data
   
   	def __setitem__(self, key, item):
   		self.data[str(key)] = item 
   ```

 - MappingProxyType(不可变映射类型): 

   ```python
   >>> from types import MappingProxyType
   >>> d = {1:'A'}
   >>> d_proxy = MappingProxyType(d)
   >>> d_proxy
   mappingproxy({1: 'A'})
   >>> d_proxy[1] 
   'A'
   >>> d_proxy[2] = 'x' 
   Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   TypeError: 'mappingproxy' object does not support item assignment
   >>> d[2] = 'B'
   >>> d_proxy 
   mappingproxy({1: 'A', 2: 'B'})
   >>> d_proxy[2]
   'B'
   ```

 - \__slots__ 属性可以改变实例属性的存储方式,由 dict 变成 tuple

 - 如果你在迭代一个字典的所有键的过程中同时对字典进行修改,那么这个循环很有可能会跳过一些键——甚至是跳过那些字典中已经有的键。
   由此可知,不要对字典同时进行迭代和修改。如果想扫描并修改一个字典,最好分成两步来进行:首先对字典迭代,以得出需要添加的内容,把这些内容放在一个新字典里;迭代结束之后再对原有字典进行更新。


### 第四章 文本

 - bytes 和  bytearray

   ```python
   >>> cafe = bytes('café', encoding='utf_8') 
   >>> cafe
   b'caf\xc3\xa9'
   >>> cafe[0]   # 各个元素是 range(256) 内的整数
   99
   >>> cafe[:1]  # bytes 对象的切片还是 bytes 对象,即使是只有一个字节的切片。
   b'c'
   >>> cafe_arr = bytearray(cafe)
   >>> cafe_arr  # bytearray 对象没有字面量句法,而是以 bytearray() 和字节序
   			  # 列字面量参数的形式显示。
   bytearray(b'caf\xc3\xa9')
   >>> cafe_arr[-1:]    # bytearray 对象的切片还是 bytearray 对象
   bytearray(b'\xa9')
   ```

 - my_bytes[0] 获取的是一个整数,而 my_bytes[:1] 返回的是一个长度为 1 的 bytes 对象——这一点应该不会让人意外。s[0] == s[:1] 只对 str 这个序列类型成立。不过,str类型的这个行为十分罕见。对其他各个序列类型来说,s[i] 返回一个元素,而 s[i:i+1] 返回一个相同类型的序列,里面是 s[i]元素。

### 第五章 一等函数

 - 函数 内省

   ```python
   >>> from clip import clip
   >>> from inspect import signature
   >>> sig = signature(clip)
   >>> sig # doctest: +ELLIPSIS
   <inspect.Signature object at 0x...>
   >>> str(sig)
   '(text, max_len=80)'
   >>> for name, param in sig.parameters.items():
   ... 	print(param.kind, ':', name, '=', param.default)
   ...
   POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
   POSITIONAL_OR_KEYWORD : max_len = 80
   ```

   kind 属性的值是 _ParameterKind 类中的 5 个值之一:

   - POSITIONAL_OR_KEYWORD : 可以通过定位参数和关键字参数传入的形参(多数 Python函数的参数属于此类)。
   - VAR_POSITIONAL : 定位参数元组。
   - VAR_KEYWORD : 关键字参数字典。
   - KEYWORD_ONLY : 仅限关键字参数(Python 3 新增)。
   - POSITIONAL_ONLY : 仅限定位参数;目前,Python 声明函数的句法不支持,但是有些使用 C 语言实现且不接受关键字参数的函数(如 divmod)支持
   - inspect.Signature 对象有个 bind 方法,它可以把任意个参数绑定到签名中的形参上,所用的规则与实参到形参的匹配方式一样。框架可以使用这个方法在真正调用函数前验证参数

### 第六章 使用一等函数实现设计模式

 - 策略模式:  定义一系列算法,把它们一一封装起来,并且使它们可以相互替换。本模式使得算法可以独立于使用它的客户而变化。
 - 命令模式: “命令”设计模式也可以通过把函数作为参数传递而简化。“命令”模式的目的是解耦调用操作的对象(调用者)和提供实现的对象(接收者)。

### 第七章 函数装饰器

 - functools.lru_cache :  它把耗时的函数的结果保存起来,避免传入相同的参数时重复计算

   ```python
   import functools
   
   @functools.lru_cache() 
   def fibonacci(n):
   	if n < 2:
   		return n
   	return fibonacci(n-2) + fibonacci(n-1)
   if __name__=='__main__':
   print(fibonacci(6))
   ```

   接受参数 maxsize, typed

   functools.lru_cache(maxsize=128, typed=False)

 - functools.singledispatch

   ```python
   from functools import singledispatch
   from collections import abc
   import numbers
   import html
   
   @singledispatch 
   def htmlize(obj):
   	content = html.escape(repr(obj))
   	return '<pre>{}</pre>'.format(content)
   
   @htmlize.register(str) 
   def _(text):
   	content = html.escape(text).replace('\n', '<br>\n')
   	return '<p>{0}</p>'.format(content)
   
   @htmlize.register(numbers.Integral) 
   def _(n):
   	return '<pre>{0} (0x{0:x})</pre>'.format(n)
   
   @htmlize.register(tuple) 
   @htmlize.register(abc.MutableSequence)
   def _(seq):
   	inner = '</li>\n<li>'.join(htmlize(item) for i
   ```

   给函数的不同类型参数定义不同的处理方法

### 第八章 对象引用、可变性、垃圾回收

- 
 - 

### 第十章

- \_\_getitem\_\_

  ```python
  >>> class MySeq:
  ...     def __getitem__(self, index):
  ...         return index 
  ...
  >>> s = MySeq()
  >>> s[1] 
  1
  >>> s[1:4] 
  slice(1, 4, None)
  >>> s[1:4:2] 
  slice(1, 4, 2)
  >>> s[1:4:2, 9] 
  (slice(1, 4, 2), 9)
  >>> s[1:4:2, 7:9] 
  (slice(1, 4, 2), slice(7, 9, None))
  ```

- 如果没有 \_\_iter\_\_ 和 \_\_contains\_\_ 方法,Python 会调用 \_\_getitem\_\_ 方法,设法让迭代和 in 运算符可用。

### 第十四章

- 可迭代对象:  实现 \_\_iter\_\_ 方法

- 迭代器  :       实现 \_\_iter\_\_ 和  \_\_next\_\_ 方法  

- 生成器用于生成供迭代的数据

- 协程是数据的消费者

- 为了避免脑袋炸裂,不能把这两个概念混为一谈

- 协程与迭代无关

- 注意,虽然在协程中会使用 yield 产出值,但这与迭代无关

  