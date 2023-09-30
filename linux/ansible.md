# Install

```shell
sudo yum install epel-release
sudo yum install ansible
```

```shell
# install ansible by pip
python3 -m pip install --user ansible
```

# practice

```shell
docker pull chusiang/ansible-managed-node:ubuntu-20.04

docker run --name server1 -d -P chusiang/ansible-managed-node:ubuntu-20.04
docker run --name server2 -d -P chusiang/ansible-managed-node:ubuntu-20.04
```

ansible.cfg
```shell
[defaults]
inventory = hosts
remote_user = docker
host_key_checking = False
```

host
```shell
server1  ansible_ssh_host=127.0.0.1  ansible_ssh_port=32768 ansible_ssh_pass=docker
server2  ansible_ssh_host=127.0.0.1  ansible_ssh_port=32769 ansible_ssh_pass=docker

[local]
server1
server2
```

验证
```shell
ansible local -m ping
```

# Ansible playbook

# Reference

[ansible.md  jaywcjlove/reference](https://github.com/jaywcjlove/reference/blob/ecb59d8980f3da31f547f4b4123d65ea395dd59c/docs/ansible.md#L4)

[chusiang/automate-with-ansible: 《現代 IT 人一定要知道的 Ansible 自動化組態技巧》](https://github.com/chusiang/automate-with-ansible)

[ansible-lint](https://github.com/ansible/ansible-lint)
