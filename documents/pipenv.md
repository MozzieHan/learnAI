### 安装pipenv
```shell
sudo apt install pipenv  # ubuntu
brew install pipenv  # macos
```

### 常用操作
- pipenv --three/--two   # 用python3/2创建一个virtualenv
- pipenv --where         # 项目根目录
- pipenv --venv          # virtualenv 所在地
- pipenv --rm            # 删除 virtualenv
- pipenv install         # 按照包
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