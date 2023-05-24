# Digger-helper

[Open-digger 官网链接](http://www.x-lab.info/open-digger/#/zh-cn/)

## 1 使用说明

### 1.1 指标查询

#### 1.1.1 仓库指标查询

```bash
python -m diggerhelper query repo
```

附加参数：

| 参数                     | 含义                              |
|------------------------|---------------------------------|
| -h, --help             | show this help message and exit |
| -n NAME, --name NAME   | The name of the repository      |
| --metric METRIC        | The metric of query             |
| --time TIME (Optional) | Category result based on time   |

完整举例：

```bash
python -m diggerhelper query repo --name aaa --metric OpenRank --time 2023-05
```

#### 1.1.2 用户指标查询

命令行头部语法：

```bash
python -m diggerhelper query user
```

附加参数：

| 参数                     | 含义                              |
|------------------------|---------------------------------|
| -h, --help             | show this help message and exit |
| -n NAME, --name NAME   | The name of the repository      |
| --metric METRIC        | The metric of query             |
| --time TIME (Optional) | Category result based on time   |

完整举例：

```bash
python -m diggerhelper query user --name aaa --metric OpenRank
```

### 1.2 指标导出

#### 1.2.1 文件导出

命令行头部语法：

```bash
python -m diggerhelper export download
```

附加参数：

| 参数                      | 含义                              |
|-------------------------|---------------------------------|
| -h, --help              | show this help message and exit |
| --query repo/user       | The type of query               |
| -n NAME, --name NAME    | The name of the repository      |
| --metric METRIC         | The metric of query             |
| --time TIME (Optional)  | Category result based on time   |
| --type json/pdf/jpg/png | The type of output file         |
| -o PATH, --output PATH  | The path of output file         |

完整举例：

```bash
python -m diggerhelper export download --query repo --name aaa --metric OpenRank --time 2023-05 --type json -o ./result.json
```

#### 1.2.2 网页导出

命令行头部语法：

```bash
python -m diggerhelper export web
```

附加参数：

| 参数                      | 含义                              |
|-------------------------|---------------------------------|
| -h, --help              | show this help message and exit |
| --query repo/user       | The type of query               |
| -n NAME, --name NAME    | The name of the repository      |
| --metric METRIC         | The metric of query             |
| --time TIME (Optional)  | Category result based on time   |

完整举例：

```bash
python -m diggerhelper export web --query user --name aaa --metric OpenRank
```
