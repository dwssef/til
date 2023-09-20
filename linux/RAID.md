# RAID

`redundant array of independent disks`(独立磁盘冗余阵列) is a data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of `data redundancy`, `performance imporvement`, or `both`.

# Standard levels

| RAID级别 | 描述|
| --------- | ------------------------------------------------ |
| RAID 0    | 数据分散存储在多个驱动器上(至少2块)，提高性能(带宽加倍)，没有冗余|
| RAID 1    | 数据通过镜像存储在两个驱动器上，提供冗余性|
| RAID 2    | 通过位级别的奇偶校验来实现冗余|
| RAID 3    | 使用独立的奇偶校验驱动器，提供冗余性|
| RAID 4    | 数据块级别的奇偶校验，提供冗余性|
| RAID 5    | 使用分布式奇偶校验，提供冗余性|
| RAID 6    | 类似于RAID 5，但提供更高级别的冗余性|
| RAID 10   | RAID 1+0，将RAID 1和RAID 0组合，提供性能和冗余|

[RAID 10/01 的区别](https://zh.wikipedia.org/zh-hans/RAID#:~:text=%E9%AB%98%E6%98%82%E3%80%82%5B5%5D-,RAID%2010/01,-%5B%E7%BC%96%E8%BE%91%5D)

# example
参照实验手册V1.0-云存储技术与应用-构建内置存储系统

环境准备:

    CentOS 7.2 Linux

    mdadm-3.4-14.el7_3.1.x86_64

所需命令:

```shell
# 查看磁盘情况
fdisk -l

# 为指定磁盘分区 (都分配:+5G) w 保存
fdisk /dev/vda

# 安装mdadm
yum install -y mdadm

# 创建 RAID 0
mdadm -Cv /dev/md0 -l0 -n2 /dev/vda[3,5]

# 查看系统上创建的 RAID 
cat /proc/mdstat

# 查看 RAID 详细信息
mdadm -D /dev/md0

# 如何删除RAID 0, 并移除RAID 0 的组成磁盘
mdadm --stop /dev/md0
mdadm --misc --zero-superblock /dev/vda3
mdadm --misc --zero-superblock /dev/vda5

# 创建 RAID 1
mdadm -Cv /dev/md0 -l1 -n2 /dev/vda[3,5]

# 创建 RAID 5
mdadm -Cv /dev/md0 -l5 -n3 /dev/vda[3,5,6]

# 格式化, 并挂载 RAID (验证)
mkfs.ext4 /dev/md0
mount /dev/md0 /mnt/
df -h

# 解挂载
umount /mnt/
# 创建 RAID 10
mdadm -Cv /dev/md0 -l10 -n4 /dev/vda[3,5,6,7]

# 创建 RAID 5, 并添加热备盘
mdadm -Cv /dev/md0 -l5 -n3 /dev/vda[3,5,6] --spare-devices=1 /dev/vda7

# 模拟硬盘故障(删除故障盘), 并查看 RAID 信息, 热备盘是否被用于重建数据
mdadm -f /dev/md0 /dev/vda3
cat /proc/mdstat
mdadm -D /dev/md0

# 移除故障盘
mdadm -r /dev/md0 /dev/vda3
```

# Term

hs: hot spare

# Reference

[RAID - 维基百科](https://zh.wikipedia.org/zh-hans/RAID)

