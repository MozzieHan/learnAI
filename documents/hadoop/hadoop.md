## hadoop

### 环境搭建

1. 创建用户

   ```shell
   useradd -m hadoop -s /bin/shell
   passwd hadoop
   adduser hadooop sudo  
   ```

2. 安装ssh， 设置ssh无密码登录

   ```shell
   sudo apt install openssh-server
   ssh localhost
   ssh-keygen -t rsa
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   ```

3. java 安装

    - 下载/解压java
    ```shell
    sudo mkdir /usr/local/jvm
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz
    sudo tar -zxvf jdk-8u191-linux-x64.tar.gz -C /usr/local/jvm/
    cd /usr/local/jvm
    sudo mv jdk1.8.0_191/ java
    ```
    - 配置环境变量/etc/profile
    ```shell
    export JAVA_HOME=/usr/local/jvm/java
    export JRE_HOME=${JAVA_HOME}/jre
    export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
    export PATH=${JAVA_HOME}/bin:$PATH
    ```

4. hadoop 安装/配置

    - hadoop 下载/解压
    ```shell
    wget http://archive-primary.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.7.0.tar.gz
    sudo tar -zxvf hadoop-2.6.0-cdh5.7.0.tar.gz -C /usr/local/
    sudo mv hadoop-2.6.0-cdh5.7.0/ hadoop
    sudo chown hadoop:hadoop hadoop
    ```
    - 配置环境变量~/.bashrc
    ```shell
    export HADOOP_HOME=/usr/local/hadoop
    export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
    export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
    export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
    ```
    - hadoop-env.sh
    ```shell
    export JAVA_HOME=/usr/local/jvm/java
    ```
    - core-site.xml
    ```xml
    <configuration>
       <property>
           <name>fs.defaultFS</name>
           <value>hdfs://localhost:8020</value>
       </property>
       <property>
           <name>hadoop.tmp.dir</name>
           <value>file:/usr/local/hadoop/tmp</value>
       </property>
    </configuration>
    ```
    - hdfs-site.xml
    ```xml
    <configuration>
        <property>
            <name>dfs.replication</name>
            <value>1</value>
        </property>
        <property>
            <name>dfs.namenode.name.dir</name>
            <value>file:/usr/local/hadoop/tmp/dfs/name</value>
        </property>
        <property>
            <name>dfs.datanode.data.dir</name>
            <value>file:/usr/local/hadoop/tmp/dfs/data</value>
        </property>
    </configuration>
    ```
    - mapred-site.xml
    ```xml
    <configuration>
        <property>
            <name>mapreduce.framework.name</name>
            <value>yarn</value>
        </property>
    </configuration>
    ```
    - yarn-site.cml 
    ```xml
    <configuration>
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
        <property> 
            <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name> 
            <value>org.apache.hadoop.mapred.ShuffleHandler</value> 
        </property> 
    </configuration>
    ```
    - 格式化namenode
    ```shell
    hdfs namenode -format
    ```

5. mysql 安装

    - 安装
    ```shell
        sudo apt install mysql-server
        sudo apt install mysql-client
        sudo apt install libmysqlclient-dev
    ```
    - 创建hive用户
    ```sql
        mysql> CREATE USER 'hive'@'%' IDENTIFIED BY 'hive'; 
        mysql> GRANT all on *.* to 'hive'@localhost identified by 'hive';
        mysql> flush privileges;
    ```
    
6. hive 安装/配置

    - hive下载/解压
    ```shell
    wget http://archive-primary.cloudera.com/cdh5/cdh/5/hadoop-2.6.0-cdh5.7.0.tar.gz
    sudo tar -zxvf hive-1.1.0-cdh5.7.0.tar.gz  -C /usr/local
    cd /usr/local/hive
    sudo mv hive-1.1.0-cdh5.7.0/ hive
    sudo chown -R hadoop:hadoop hive/
    ```
    - 配置环境变量~/.bashrc
    ```shell
    export HIVE_HOME=/usr/local/hive
    export PATH=$PATH:$HIVE_HOME/bin
    ```
    - 将mysql-connector-java-5.1.31.jar 放在HIVE_HOME/lib下
    hive 配置文件
    - hive-site.xml 
    ```xml
    <configuration>
        <property>
            <name>system:java.io.tmpdir</name>
            <value>/user/hive/warehouse</value>
        </property>
        <property>
            <name>system:user.name</name>
            <value>${user.name}</value>
         </property>
         <property>
            <name>javax.jdo.option.ConnectionURL</name>
            <value>jdbc:mysql://localhost:3306/metastore?createDatabaseIfNotExist=true&amp;useSSL=false</value>      </property>      <property>         <name>javax.jdo.option.ConnectionDriverName</name>
            <value>com.mysql.jdbc.Driver</value>
         </property>
         <property>
            <name>javax.jdo.option.ConnectionUserName</name>
            <value>hive</value>
            <description>user name for connecting to mysql server</description>
        </property>
        <property>
            <name>javax.jdo.option.ConnectionPassword</name>
            <value>hive</value>
            <description>password for connecting to mysql server</description>
        </property>
    </configuration>
    ```
    - 初始化mysql数据库
    ```shell
    schematool -dbType mysql -initSchema
    ```
    
7. pyhive 安装

    ```shell
    sudo apt install python3-dev
    sudo apt install libsasl2-dev
    sudo apt install pipenv
    pipenv install pyhive
    mkdir testhive
    cd testhive
    pipenv --three
    pipenv install pyhive
    pipenv install thrift
    pipenv install sasl
    pipenv install thrift-sasl
    ```

8. hbase 安装/配置

    - hbase 下载/解压
    ```shell
    wget http://archive-primary.cloudera.com/cdh5/cdh/5/hbase-1.2.0-cdh5.7.0.tar.gz
    sudo tar -zxvf hbase-1.2.0-cdh5.7.0.tar.gz -C /usr/local/
    cd /usr/local
    sudo mv hbase-1.2.0-cdh5.7.0 hbase
    sudo chown -R hadoop:hadoop hbase
    ```
    - 环境变量 ~/.bashrc
    ```shell
    export HBASE_HOME=/usr/local/hbase
    export PATH=$PATH:$HBASE_HOME/bin
    ```
    - hbase-sit.xml
    ```xml
    <configuration>
        <property>
            <name>hbase.rootdir</name>
            <value>file:///usr/local/hbase/tmp</value>
        </property>
    </configuration>
    ```
    
9. zookeeper 安装/配置

    - zookeeper 下载/解压
    ```shell
    wget http://archive-primary.cloudera.com/cdh5/cdh/5/zookeeper-3.4.5-cdh5.7.0.tar.gz
    sudo tar -zxvf zookeeper-3.4.5-cdh5.7.0 -C /usr/local/
    cd /usr/local
    sudo mv zookeeper-3.4.5-cdh5.7.0 zookeeper
    sudo chown -R hadoop:hadoop zookeeper
    ``` 
    - 环境变量 ~/.bashrc
    ```shell
    export ZOOKEEPER_HOME=/usr/local/zookeeper
    export PATH=$PATH:$ZOOKEEPER_HOME/bin
    export ZOO_LOG_DIR=$ZOOKEEPER_HOME/logs
    ```

### HDFS

master/slave 架构 （namenode,  datanode)

1个文件拆分多个block 

blocksize: 128M(默认)

130M --> 2个block（128M+2M）

#### hdfs 常用命令

| 选项名称 | 使用格式 | 含义 |
| -------- | :------- | ---- |
| -ls| -ls <路径> |查看指定路径的当前目录结构：|
| -lsr | -lsr <路径> |递归查看指定路径的目录结构|
| -du |-du <路径>| 统计目录下个文件大小|
| -dus |-dus <路径>| 汇总统计目录下文件(夹)大小|
| -count | -count [-q] <路径> 统计文件(夹)数量 ||
| -mv  | -mv <源路径> <目的路径> | 移动 |
| -cp  | -cp <源路径> <目的路径> | 复制 |
| -rm  | -rm [-skipTrash] <路径> | 删除文件/空白文件夹 |
|-rmr| -rmr [-skipTrash] <路径> |递归删除|
|-put |-put <多个 linux 上的文件> <hdfs 路径>| 上传文件|
|-copyFromLocal| -copyFromLocal <多个 linux 上的文件> <hdfs 路径> |从本地|
|-moveFromLocal |-moveFromLocal <多个 linux 上的文件> <hdfs 路径>|从本地移动|
|-getmerge| -getmerge <源路径> <linux 路径> |合并到本地|
|-cat |-cat <hdfs 路径>| 查看文件内容|
|-text |-text <hdfs 路径>| 查看文件内容|
|-copyToLocal |-copyToLocal [[-ignoreCrc][-crc][hdfs 源路径][linux 目的路径]|从本地复制|
|-moveToLocal |-moveToLocal [-crc] <hdfs 源路径> <linux 目的路径>| 从本地移动|
|-mkdir |-mkdir <hdfs 路径>| 创建空白文件夹|
|-setrep |-setrep [-R][-w] <副本数> <路径>| 修改副本数量|
|-touchz |-touchz <文件路径>| 创建空白文件|
|-stat |-stat [format] <路径> |显示文件统计信息|
|-tail |-tail [-f] <文件>| 查看文件尾部信息|
|-chmod |-chmod [-R] <权限模式> [路径] |修改权限|
|-chown |-chown [-R][属主][:[属组]] 路径 |修改属主|
|-chgrp |-chgrp [-R] 属组名称 路径 |修改属组|
|-help |-help [命令选项]| 帮助|

### YARN

不同计算框架可以共享同一个hdfs集群上的数据，享受整体的资源调度

#### 架构

- ResourceManager：RM
  - 整个集群同一时间提供服务只有一个（一般存在2个，1主1备），负责集群资源的统一管理和调度
  - 处理客户端请求： 提交作业，杀死作业
  - 监控NM，一旦某个NM挂了，那么该NM上运行的任务需要告诉AM来如何进行处理
- NodeManager：NM
  - 有多个，负责自己本身节点资源管理和使用
  - 定时向RM汇报本节点的资源使用情况
  - 接受并处理来自RM的各种命令：启动Container
  - 处理来自AM的命令
  - 单个节点的资源管理
- ApplicationMaster： AM
  - 每个程序对应一个（一个mapreduce，一个spark），负责应用程序的管理
  - 为应用程序向RM申请资源（core，memory）， 分配给内部task
  - 需要与NM通信：启动/停止task，task是运行在container里面，AM也是运行在container里面
- Container
  - 封装了CPU，memory等资源的一个容器
  - 是一个任务运行环境的抽象
- Client
  - 提交作业
  - 查询作业的进度
  - 杀死作业

### MapReduce

#### mapper 任务详解

1. **split**: split size=block size, 每个切片由一个MapTask 处理
2. 按照一定的规则解析成<key, value>对。默认把每一行文本内容解析超那个键值对, key 是没一行的起始位置，value是本行内容
3. **map**: 对上阶段中的每个k, v调用一次mapper类的map方法，每次输出0个或多个键值对
4. 按照一定规则对上一阶段输出的键值对进行分区，默认只有一个区，分区的数量就是reduce任务运行的数量
5. 对每个分区的键值对进行排序，首先,按照键进行排序,对于键相同的键值对,按照值进行排序。比如三个键值对<2,2>、<1,3>、<2,1>,键和值分别是整数。那么排序后的结果是<1,3>、<2,1>、<2,2>。如果有第六阶段,那么进入第六阶段;如果没有,直接输出到文件中
6. **combiner**: 对数据进行局部聚合处理。本阶段默认没有

#### reduce任务详解

1. Reducer 任务会主动从 Mapper 任务复制其输出的键值对。Mapper 任务可能会有很多,因此 Reducer 会复制多个 Mapper 的输出
2. 把复制到 Reducer 本地数据,全部进行合并,即把分散的数据合并成一个大的数据。再对合并后的数据排序
3. 是对排序后的键值对调用 reduce 方法。键相等的键值对调用一次reduce 方法,每次调用会产生零个或者多个键值对。最后把这些输出的键值对写入到 HDFS 文件中。

### hadoop 生态

- hive HQL  提供基于hdfs类sql查询，离线批处理
- hbase     分布式数据库（基于hdfs） # 也可基于本地文件系统/亚马逊s3
- zookeeper 分布式协调框架
- flume     日志收集         日志文件-->hdfs/hive/hbase/...
- sqoop     数据库数据收集    关系数据库<-->hdfs/hive/hbase/...
- spark     可代替mapreduce,加快处理速度 / hive on spark / spark streaming做流处理
- kafka     分布式消息队列
