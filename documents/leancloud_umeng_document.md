### leancloud im 

#### 核心概念

- clientId： 每一个终端为一个clientId, 在应用内唯一，相当于一个单独的用户。本项目中采用uuid4，取user.uid。leancloud默认允许一个clientId在多个设备登录。

- 在线状态： leancloud在SDK和RESTAPI上提供查询目标用户的在线状态。

- 对话(conversation)： 用户登录后，与其他人今夕消息沟通，即为开启一个conversation。开始聊天前，需要先创建或加入一个对话，然后在邀请其他人进来。所有消息都是由某一个client 发往一个 conversation。

  _Conversation表中字段名与对话的各个属性对应关系：

  | 表字段       | 属性名         | 类型    | 约束 | 说明                                                         |
  | ------------ | -------------- | ------- | ---- | ------------------------------------------------------------ |
  | **attr**     | attributes     | Object  | 可选 | 自定义属性，供开发者扩展使用。                               |
  | **objectId** | conversationId | String  |      | 对话 id（只读），由云端为该对话生成的一个全局唯一的 id。     |
  | **c**        | creator        | String  |      | 对话创建者的 clientId（只读）                                |
  | **lm**       | lastMessageAt  | Date    |      | 对话中最后一条消息的发送或接收时间                           |
  | **m**        | members        | Array   |      | 普通对话的所有参与者（仅针对普通对话，暂态对话和系统对话并不支持持久化的成员列表） |
  | **mu**       | mute           | Array   |      | 将对话设为静音的参与者，这部分参与者不会收到推送。 （仅针对 iOS 以及 Windows Phone 用户有效） |
  | **name**     | name           | String  | 可选 | 对话的名字，可为群组命名。                                   |
  | **tr**       | transient      | Boolean | 可选 | 是否为暂态对话                                               |
  | **sys**      | system         | Boolean | 可选 | 是否是系统对话                                               |
  | **unique**   | unique         | Boolean | 可选 | 内部字段，标记根据成员原子创建的对话。                       |

- 创建对话： 普通对话通过SDK创建， 暂态对话跟系统对话通过REST API 创建。本项目中只用到普通对话。由于业务中所有的聊天都为单聊。故创建conversation是 **unique** 选 **True**， 这样之前如果有相同clientId创建的conversation会复用，而不会新建conversation。

- 消息(message)： 即时通讯服务的消息，leancloud允许一次传输不超过5kb的文本数据.系统对消息格式没有任何要求，可以在文本协议基础上定义自己的应用层协议。一个对话的消息记录会在leancloud云端保留6个月。

  消息格式： 

  | 参数       | 约束 | 说明                                                         |
  | ---------- | ---- | ------------------------------------------------------------ |
  | `_lctype`  |      | 富媒体消息的类型   <br>-    消息          类型  <br>- 文本消息        -1    <br>- 图像消息        -2    <br/>- 音频消息        -3    <br/>- 视频消息        -4    <br/>- 位置消息        -5    <br/>- 文件消息        -6    <br/>- 活动消息         1 |
  | `_lctext`  |      | 富媒体消息的文字说明                                         |
  | `_lcattrs` |      | JSON 字符串，用来给开发者存储自定义属性。                    |
  | `_lcfile`  |      | 如果是包含了文件（图像、音频、视频、通用文件）的消息 ， `_lcfile` 就包含了它的文件实体的相关信息。 |
  | `url`      |      | 文件在上传之后的物理地址                                     |
  | `objId`    | 可选 | 文件对应的在 `_File` 表里面的 objectId                       |
  | `metaData` | 可选 | 文件的元数据                                                 |

  活动消息格式：

  ```json
  {
      "_lctype": 1,
      "_lctext": {
          "id": 1,
          "title": "活动1",
          "start": "活动开始时间",
          "address": "活动地址"
      }
  }
  ```

- 敏感词过滤： leancloud为多人的普通对话，暂态对话，系统对话进行敏感词过滤。词库由leancloud提供，替换为×××，支持用户自定义敏感词过滤。
- 权限跟认证： 使用签名可以保证聊天通道的安全，这一功能默认是关闭的，可以在 [控制台 > 消息 > 实时消息 > 设置 > 实时消息选项] 中进行开启（目前我们启用登录认证）：
  - **登录启用签名认证**，用于控制所有的用户登录
  - **对话操作启用签名认证**，用于控制新建或加入对话、邀请/踢出对话成员等操作
  - **聊天记录查询启用签名认证**，用于控制聊天记录查询操作

####  聊天时序图

```sequence
participant client
participant server
participant leancloud server
client -> server: 请求签名
server -> client: 返回签名
client -> leancloud server: 带着签名登录leancloud服务器, 建立链接
client -> leancloud server: 创建conversation,开始聊天
```

#### 签名

leancloud 签名采用 Hmac-sha1 算法

leancloud支持登录签名，开启会话签名，查询聊天记录签名。

- 登录签名msg 格式 "appid:clientid::timestamp:nonce"
  - appid  应用appid
  - clientid  登录使用的clientid, 对应我们项目的user.uid
  - timestamp   当前时间戳，ms 单位
  - nonce 随机字符串
- 开启对话签名   "appid:clientid:sorted_member_ids:timestamp:nonce"
  - sorted_member_ids  是以半角冒号（:）分隔、升序排序 的 user id，即邀请参与该对话的成员列表
- 查询聊天记录签名  "appid:client_id:convid:nonce:signature_ts"
  - signature_ts 签名时间戳 单位s

### umeng push message 

umeng push 消息一共有3种类型

- Unicast  单播， 向一个device token 推送消息
- Listcast  列播， 向多个device token 推送消息， 最大500个，用逗号隔开
- Broadcast  广播， 向所有设备推送消息

友盟推送消息时 android 和 ios 是两个应用，需要完全分

目前定义好的推送消息（目前所有推送消息均为unicast）

```json
{
    101: {
        "title": "用户审核",
        "text": "很抱歉,您的照片未通过审核,建议上传本人真实相片哦",
        "push_type": "unicast",
    },
    102: {
        "title": "匹配成功",
        "text": "有人对你产生好感,打开看看吧",
        "push_type": "unicast",
    },
    201: {
        "title": "用户被举报",
        "text": "很抱歉,您被多次投诉已进入黑名单",
        "push_type": "unicast",
    },
    202: {
        "title": "被投诉提醒",
        "text": "您已被投诉2次,请注意措辞啊",
        "push_type": "unicast",
    },
    301: {
        "title":"成功报名",
        "text": "您已成功报名参加了《{}》",
        "push_type": "unicast",
    },
}
```

