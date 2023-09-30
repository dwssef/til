# Install python (manually)
[Index of /ftp/python/](https://www.python.org/ftp/python/)
```shell
sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel

wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz

tar -xvf Python-3.9.6.tgz

./configure --enable-optimizations

sudo make

sudo make altinstall
```

# Install python (pyenv)
[pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)

```shell
# centos7.9
# https://github.com/pyenv/pyenv/issues/2416#issuecomment-1491244200

yum install gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel git libffi-devel
yum install epel-release
yum install openssl11 openssl11-devel
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
export CFLAGS=$(pkg-config --cflags openssl11)
export LDFLAGS=$(pkg-config --libs openssl11)
mkdir -p ~/tmp
export TMPDIR=~/tmp
pyenv install 3.10.4
pyenv versions
```

# Common Commands

```shell
# help
pyenv command
pyenv help <command>

# show python versions
pyenv install -l

# 下载安装不同python版本
pyenv install 3.11.5

pyenv versions

# 为当前shell设置python环境
pyenv shell <版本> 或 <虚拟环境名>

# 全局设置
pyenv global 3.11.5

# 当前目录及其子目录的python环境
pyenv local 3.11.5

# 创建虚拟环境
pyenv virtualenv <版本> <虚拟环境名>

# 列出虚拟环境
pyenv virtualenvs 

# 激活虚拟环境
pyenv activate env-name 

# 退出虚拟环境
pyenv deactivate

# 删除虚拟环境
pyenv uninstall env-name  
```

# hiw
利用环境变量来指定当前python环境
```shell
$ export | grep pyenv
PATH='/home/dw/.pyenv/shims:/...
```