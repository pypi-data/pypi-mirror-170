# pyhanzi


## 发布

```bash
python3 -m venv pyhanzi-venv/
source pyhanzi-venv/bin/activate.fish

# 调试好之后
python3 -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
pip3 install -i https://mirrors.aliyun.com/pypi/simple/ setuptools wheel
python3 setup.py sdist bdist_wheel

pip3 freeze > requirements.txt
# requirements添加一个peppercorn
echo 'peppercorn' >> requirements.txt
pip3 download -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ -d dist/

cd dist/
dir2pi -S .
scp -r simple/ root@39.97.232.223:/root/pypi/
pip3 install -i http://www.hohohaha.cn:8000/simple/ pyhanzi==0.0.2 --trusted-host www.hohohaha.cn
```

## 上传到pypi

```bash
# python3 -m venv pyhanzi-venv/
source pyhanzi-venv/bin/activate.fish
rm -rf dist/*
python3 setup.py sdist bdist_wheel
pip3 install -i https://mirrors.aliyun.com/pypi/simple/ twine
python3 -m twine upload dist/*
```

## 安装

```bash
pip3 install -i https://pypi.python.org/simple pyhanzi==0.0.9
```
