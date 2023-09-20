# NAT

网络地址转换（Network Address Translation）简称为NAT，是将IP数据包包头中的IP地址转换为另一个IP地址的协议
路由器网关会将IP数据包进行地址转换

PC -> NAT -> Internet

# SNAT
Source Network Address Translation
防止外部源直接访问后端实例

VM -> SNAT -> Internet
VM <- SNAT <- Internet

## 示例

```shell
# 上述配置将所有从192.168.1.0/24子网发送到外部网络的请求的源IP地址转换为11.22.33.44
iptables -t nat -A POSTROUTING -o eth0 -s 192.168.1.0/24 -j SNAT --to-source 11.22.33.44
```


# DNAT
Destination Network Address Translation

client -> Internet -> DNAT -> Server
client <- Internet <- DNAT <- Server

## 示例

```shell
# 将eth0网口发往80端口的包，都转发到内网192.168.1.100:80上
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.100:80
```

# Reference

[SNAT和DNAT的区别 - SegmentFault 思否](https://segmentfault.com/q/1010000002389520)