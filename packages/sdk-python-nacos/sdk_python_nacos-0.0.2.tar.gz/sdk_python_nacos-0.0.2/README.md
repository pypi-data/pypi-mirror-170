build = python3 setup.py sdist
install = python3 setup.py install
publish = python3 setup.py register && python3 setup.py sdist upload


## twine 是一个专门用于与 pypi 进行交互的工具
```
pip3 install twine
# 升级打包工具
python3 -m pip install --user --upgrade setuptools wheel
# 打包
python3 setup.py sdist bdist_wheel
# 安装测试
python3 setup.py install
# 检查
twine check dist/*
# 上传
twine upload dist/*
```

~/.pypirc
[server-login]
username = jnan77
password = xxxx