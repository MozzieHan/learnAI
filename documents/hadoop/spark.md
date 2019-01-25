### spark 基础

#### 下载/安装/配置
```shell
wget https://archive.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.6.tgz
sudo tar -zxvf spark-2.4.0-bin-hadoop2.6.tgz -C /usr/local/
sudo chown hadoop:hadoop spark-2.4.0-bin-hadoop2.6/
sudo mv spark-2.4.0-bin-hadoop2.6/ spark
# ~/.bashrc
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$SPARK_HOME/bin
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=ipython3
```

#### pyspark 示例
```python
# pyspark
lines = sc.textFile("README.md")
lines.count()
# >>> 105
lines.fist()
# >>> "hello world"
```

### RDD编程

spark 对数据的核心抽象--弹性分布式数据集(Resilient Distribute Dataset). 
在spark中,对数据是操作
- 创建RDD
- 转化已有RDD
- 调用RDD操作进行求值

#### RDD 基础
RDD 就是一个不可变的分布式对象那个集合.
- 创建RDD
    lines = sc.textFile("README.MD")
- 转化操作(transformation)  

    转化操作会由一个RDD 生成一个新的RDD
    转化操作反会的是RDD对象, 而行动操作返回的是 其他数据类型
    python_line = lines.filter(lambda line: "python" in line)
- 行动操作(action)   
    
    行动操作会对一个RDD计算出一个结果, 并把结果返回到驱动器中,或把结果存储到外部存储系统(如HDFS)
    python_line.first()
    
spark 惰性计算RDD, 每次action 都会重新计算, 可以用 persist() 把数据的持久化
```python
python_line.persist()
python_line.count()
python_line.first()
```

每个spark程序或shell会话都按如下方式工作
- 从外部数据创建输入RDD
- 使用像first()这样的转化操作对RDD进行转化,以定义新的RDD
- 告诉spark对需要被重用的中间结果RDD执行persist()操作
- 使用行动操作来触发一次并行计算,spark会对计算进行优化后再执行

1. 创建RDD
    ```python
    # 1.
    lines = sc.parallelize(["pandas", "i like pandas"])
    # 2.
    lines = sc.textFile("README.md")
    ```

2. 转化操作
    
    
    
#### pyspark 操作
```python
# 创建RDD
line = sc.parallelize(["i", "love", "python", "i love python"])
line2 = sc.textFile("README.md")

# 转化操作RDD
line3 = line.filter(lambda x: "love" in x)  # 返回包含 love 的行的RDD
line4 = line.map(lambda x: "new" + x)  # 每行前加上 new
line5 = line.flatMap(lambda x: line.split(" "))  # 将数据切分为单词
line6 = line.union(line3)

# 内存缓存RDD
line.persist()

# 行动操作
line.count()
line.first()
line.task(10)  # 返回 line 的前10个元素
# collect 不能用在大规模数据集上
line.collect()  # 返回 line 的所有元素
sum = line.reduce(lambda x, y: x + y)

```

### hive, hive on spark 和 sparkSQL 区别
[hive, hive on spark, sparkSQL](https://blog.csdn.net/MrLevo520/article/details/76696073)


### spark streaming
