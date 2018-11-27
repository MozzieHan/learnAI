### 安装/配置
- 下载/解压
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
        <value>hdfs://localhost:8020/tmp/hbase</value>
    </property>
    <property>
        <name>hbase.zookeeper.quorum</name>
        <value>localhost</value>
    </property>
    <property>
        <name>hbase.zookeeper.property.clientPort</name>
        <value>2181</value>
    </property>

    <property>
        <name>hbase.cluster.distributed</name> 
        <value>true</value>
    </property>
    <property>
        <name>hbase.zookeeper.property.dataDir</name>
        <value>/usr/local/zookeeper/tmp</value>
    </property>
    <property> 
        <name>hbase.tmp.dir</name> 
        <value>/usr/local/hbase/tmp</value> 
    </property>
</configuration>
```

- hbase-env.sh
```
export JAVA_HOME=/usr/local/jvm/java
export HBASE_MANAGES_ZK=false
```

### hbase 基础介绍


### hbase 操作

### python 连接hbase
启动thrift
hbase-daemon.sh start thrift 默认端口是9090
```
# 注: 此hbase库是基于python2开发,其中某些语法与python3不兼容,需修改某些源码
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import *

transport = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
transport.open()

contents = ColumnDescriptor(name='cf:', maxVersions=1)
client.createTable('test', [contents])

print(client.getTableNames())
```

[python通过thrift简单操作hbase](https://www.cnblogs.com/hitandrew/archive/2013/01/21/2870419.html)

[python3使用hbase时修改](https://blog.csdn.net/luanpeng825485697/article/details/81048468)


