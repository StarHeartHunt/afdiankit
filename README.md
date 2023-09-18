<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://raw.githubusercontent.com/StarHeartHunt/afdiankit/master/LICENSE">
    <img src="https://img.shields.io/github/license/StarHeartHunt/afdiankit" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/afdiankit">
    <img src="https://img.shields.io/pypi/v/afdiankit?logo=python&logoColor=edb641" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue?logo=python&logoColor=edb641" alt="python">
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=edb641" alt="black">
  </a>
  <a href="https://github.com/Microsoft/pyright">
    <img src="https://img.shields.io/badge/types-pyright-797952.svg?logo=python&logoColor=edb641" alt="pyright">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="ruff">
  </a>
  <a href="https://results.pre-commit.ci/latest/github/StarHeartHunt/afdiankit/master">
    <img src="https://results.pre-commit.ci/badge/github/StarHeartHunt/afdiankit/master.svg" alt="pre-commit" />
  </a>
</p>

<div align="center">

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD036 -->

_✨ 一个现代化的爱发电 Python SDK ✨_

_✨ 同时支持 **同步** 与 **异步** 调用 ✨_

</div>

## 安装方式

```bash
pip install afdiankit
# or, use poetry
poetry add afdiankit
# or, use pdm
pdm add afdiankit
```

## 使用方法

### 使用爱发电网页端 API

#### 获取网页端 `auth_token`

在爱发电网页端打开 F12 开发者工具，切换到 Console（控制台）标签页，输入以下 JavaScript 代码获取网页端 auth token

```javascript
document.cookie.match(new RegExp("(^| )auth_token=([^;]+)"))[2];
```

新建 Python 脚本，可直接复制以下模板，替换 auth_token 即可。

```python
from afdiankit import Afdian, TokenAuthStrategy

afdian = Afdian("<auth_token>")
# 或者显式调用 TokenAuthStrategy
github = GitHub(TokenAuthStrategy("<auth_token>"))
```

### 使用开放平台 API
