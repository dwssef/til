搜索查到要去做入职体检的医院19年费用是125元，23年145元，想了解平均每年的涨幅是多少
# 增长量公式

$$
growth = e^{rt}
$$

```python
import math

# 125*e**(r*4) = 145
print(math.log(145/125)/4) # 0.037105...
```

# Reference
[数学常数e的含义 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2011/07/mathematical_constant_e.html)

## TODO
sympy

检查完备?