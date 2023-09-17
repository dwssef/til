[fileinput 官方文档](https://docs.python.org/zh-cn/3/library/fileinput.html) 

fileinput: 将命令行的输入(stdin)或是文件列表作为一个迭代对象返回

## 示例
查看 docker 容器日志信息时，想知道某一条访问请求是什么时候发生的，或是想知道大量的请求之前的间隔时间。`fileinput`能实现这个功能，在每条日志前加上时间戳，在不改变原有功能的基础上，为其添加额外功能。

```shell
$ docker logs -f <容器id>
response:400
response:400
response:400
response:400
response:400
response:400
```

```python
# timestamp.py
from datetime import datetime
import fileinput
for line in fileinput.input():
    print(f'[{datetime.now()}] {line}', end='')
```

```shell
$ docker logs -f e11 | python3 timestamp.py
[2023-09-16 16:06:28.868516] response:400
[2023-09-16 16:06:28.868524] response:400
[2023-09-16 16:06:28.868532] response:400
[2023-09-16 16:06:28.868540] response:400
[2023-09-16 16:06:28.868548] response:400
[2023-09-16 16:06:28.868556] response:400
```

## 其他
配合Shell命令进行数据处理和分析
