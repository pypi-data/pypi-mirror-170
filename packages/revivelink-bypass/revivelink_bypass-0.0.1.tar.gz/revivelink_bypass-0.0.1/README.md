# revivelink bypass

<div>

| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD | [![CI - Test](https://github.com/FlorentClarret/revivelink-bypass/actions/workflows/tox.yml/badge.svg)](https://github.com/FlorentClarret/revivelink-bypass/actions/workflows/tox.yml)                                                                                                                                                                                                                                                                                                                       |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/revivelink-bypass.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/revivelink-bypass/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/revivelink-bypass.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/revivelink-bypass/) |
| Meta | [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://github.com/python/mypy) [![imports - isort](https://img.shields.io/badge/imports-isort-ef8336.svg)](https://github.com/pycqa/isort) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)                                                                    |
</div>

revivelink-bypass is a very simple open-source Python library to get links protected by [revivelink](https://revivelink.com/).

## Install

``` shell
pip install revivelink-bypass
```

## Usage

```python
from revivelink_bypass import get_links

links = get_links("http://revivelink.com/BYPASS")
```

# Contributing guide

Glad you want to help! To do so, you can read our [Contributing guide](CONTRIBUTING.md).
