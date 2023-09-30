# yum源
```shell
sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' \
         -e 's|^#baseurl=http://mirror.centos.org/centos|baseurl=https://mirrors.tuna.tsinghua.edu.cn/centos|g' \
         -i.bak \
         /etc/yum.repos.d/CentOS-*.repo
```

```shell
sudo yum makecache
```

# 卸载旧的docker
```shell
sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

# docker用户组(可选操作)

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

# docker软件源

```shell
# docker 官方源
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
# 阿里云源
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

# 安装docker

```shell
sudo yum install docker-ce
```

# 设置docker国内镜像源

添加不再提供服务的镜像加速器，会拖慢镜像拉取速度

```shell
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
    "registry-mirrors": [
        "https://docker.mirrors.sjtug.sjtu.edu.cn",
        "https://hub-mirror.c.163.com",
        "https://mirror.baidubce.com",
        "https://docker.nju.edu.cn"
    ]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

# 启动docker

```shell
sudo systemctl enable docker
sudo systemctl start docker
```

# 测试docker

```shell
docker run --rm hello-world
```

# Reference
[jaywcjlove/docker-tutorial: 🐳 Docker入门学习笔记](https://github.com/jaywcjlove/docker-tutorial)

[Install Docker Engine on CentOS | Docker Docs](https://docs.docker.com/engine/install/centos/)

[centos 清华源](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)

[国内的 Docker Hub 镜像加速器](https://gist.github.com/y0ngb1n/7e8f16af3242c7815e7ca2f0833d3ea6)

[Failed to start LSB: Bring up/down错误解决方法](https://juejin.cn/post/6981679103535480840)