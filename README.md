# README

一个比较通用的 flask 项目的模板

## 环境

> python -V 3.7.9

建立虚拟环境

```bash
mkdir venv && cd venv
python3.7 -m venv .
```

安装所需第三方库

```bash
pip install -r doc/requirements.txt [-i https://pypi.tuna.tsinghua.edu.cn/simple]
```

## 配置

- [gunicorn 参考配置](config/settings.py)
- [flask 项目参考配置](config/base.py)

## 运行

```bash
python manager.py run
```

```bash
gunicorn -c settings.py --log-level=debug --reload manager:app
```
