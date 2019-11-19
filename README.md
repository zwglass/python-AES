# python-dependencies-handle python 依赖库操作

### 1. 新建虚拟环境 并进入虚拟环境

```
# 新建空文件夹 venv
mkdir venv

# 进入 venv 文件夹
cd ./venv

# 安装虚拟环境 最后一个 . 表示安装在当前目录
python3 -m venv .

# 激活虚拟环境
source ./bin/activate

# 退出虚拟环境
deactivate

```

### 2. 运行 python 文件

```
# 运行 python 文件例子(在虚拟环境下运行)
python ./pycrypto_aes.py
```

### 3. 依赖文件一键安装

```
# 依赖文件安装: 
pip install -r requirements.txt
```
