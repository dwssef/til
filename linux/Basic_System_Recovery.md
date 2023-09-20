# Rescue Mode

- booting a small Linux environment from a USB devices, CD
- 可以将文件系统挂载为只读, 可添加或移除驱动
- 默认 root 分区是临时的 root 分区
- 可以通过`chroot /mnt/sysroot` 或 `/mnt/sysimage` 将root 分区改为文件系统的 root 分区
- 可以配置网络接口传输文件 (scp)

进入救援模式的原因通常是：
- 无法找到根文件系统(GRUB 引导被覆盖)
- 遇到了硬件或软件问题，并且想将几个重要的文件从系统硬盘中取出

# Single-user Mode

- 不需要挂载启动 CD或USB, 但不挂载文件系统，只提供一个root用户来操作, 运行在`runlevel 1`, 且无网络连接, 如果`init配置文件`受损或文件系统无法挂载, 则该模式将无法使用

进入单用户模式的原因通常是
- 重置root密码
- 基本的系统维护

# Emergency Mode

- 无法进入救援模式的情况使用
- 不激活网络接口，只启动一些基本服务
- root文件系统只读挂载, 不需要加载`init配置`

进入紧急模式的原因通常是：

- /etc/fstab文件存在错误导致挂载文件系统时失败。
- 文件系统存在错误导致。

# other
按照问题的严重性和复杂度划分的话(my opinion)

Emergency Mode > Rescue Mode > Single-user Mode

# Reference

[第 36 章 基本系统恢复 红帽企业版 Linux 6 | Red Hat Customer Portal](https://access.redhat.com/documentation/zh-cn/red_hat_enterprise_linux/6/html/installation_guide/ap-rescuemode)

[引导失败，RAID启动镜像引导](https://en.wikipedia.org/wiki/RAID#:~:text=If%20a-,boot%20drive%20fails,-%2C%20the%20system%20has)
