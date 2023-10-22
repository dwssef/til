# start up wg client 

```shell
wg-quick up $HOME/.wg0.conf
wg-quick down $HOME/.wg0.conf
```

# webUI后续禁止公网访问

prerequisite: 容器映射端口 `51821:51821`

1. 从公网访问webUI拿到配置文件
2. 防火墙禁用`51821`端口
3. 用配置文件从wg内网访问webUI

# Reference

[weejewel/wg-easy - Docker Image | Docker Hub](https://hub.docker.com/r/weejewel/wg-easy)
