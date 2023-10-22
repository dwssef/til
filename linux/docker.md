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
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
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

# docker清理

```shell
docker system prune --help
docker system prune -a --force
docker system df
```

# CUDA容器测试
```shell
docker run --rm --runtime=nvidia --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi
```


# Reference
[jaywcjlove/docker-tutorial: 🐳 Docker入门学习笔记](https://github.com/jaywcjlove/docker-tutorial)

[Install Docker Engine on CentOS | Docker Docs](https://docs.docker.com/engine/install/centos/)

[Install Docker Engine on Ubuntu | Docker Docs](https://docs.docker.com/engine/install/ubuntu/#prerequisites)

[centos 清华源](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)

[国内的 Docker Hub 镜像加速器](https://gist.github.com/y0ngb1n/7e8f16af3242c7815e7ca2f0833d3ea6)

[docker 设置国内镜像源-阿里云开发者社区](https://developer.aliyun.com/article/1294592?spm=5176.26934562.main.2.5fad7a64z41xOs)

[Failed to start LSB: Bring up/down错误解决方法](https://juejin.cn/post/6981679103535480840)

[Installing the NVIDIA Container Toolkit — NVIDIA Container Toolkit 1.14.2 documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt)

[基于 Docker 的深度学习环境：入门篇 - 苏洋博客](https://soulteary.com/2023/03/22/docker-based-deep-learning-environment-getting-started.html)

