### pipenv 介绍
pipenv 是 Pipfile 主要倡导者、requests 作者 Kenneth Reitz 写的一个命令行工具，主要包含了Pipfile、pip、click、requests和virtualenv。Pipfile和pipenv本来都是Kenneth Reitz的个人项目，后来贡献给了pypa组织。Pipfile是社区拟定的依赖管理文件，用于替代过于简陋的 requirements.txt 文件。

Pipfile的基本理念是：

Pipfile 文件是 TOML 格式而不是 requirements.txt 这样的纯文本。
一个项目对应一个 Pipfile，支持开发环境与正式环境区分。默认提供 default 和 development 区分。
提供版本锁支持，存为 Pipfile.lock。
click是Flask作者 Armin Ronacher 写的命令行库，现在Flask已经集成了它。


使用pipenv之前, 必须彻底忘记pip
### 安装pipenv
```shell
pip install pipenv  
```

### 常用操作
- pipenv --three/--two   # 用python3/2创建一个virtualenv
- pipenv --python 3.6    # 指定某一python版本创建环境
- pipenv --where         # 项目根目录
- pipenv --venv          # 显示virtualenv信息
- pipenv --py            # 显示python解释器信息
- pipenv --rm            # 删除 virtualenv
- pipenv install         # 安装模块并加入pipfile
- pipenv install --dev   # dev 安装包
- pipenv clean           # 删除所有没有在lock文件中的包
- pipenv graph           # 显示安装的所有包及依赖
- pipenv lock            # 更新lock文件
- pipenv run             # 后面跟进入env后的命令
- pipenv shell           # 进入virtualenv
- exit                   # 退出virtualenv
- pipenv sync            # 同步lock文件中的包
- pipenv uninstall       # 删除包, 并从pipfile中移除
- pipenv update          # 先执行lock, 再执行sync


pip 国内源
- 阿里云         https://mirrors.aliyun.com/pypi/simple/
- 中国科技大学    https://pypi.mirrors.ustc.edu.cn/simple/ 
- 豆瓣(douban)   https://pypi.douban.com/simple/ 
- 清华大学        https://pypi.tuna.tsinghua.edu.cn/simple/
- 中国科学技术大学 https://pypi.mirrors.ustc.edu.cn/simple/