OpenCanary
=================
Thinkst Applied Research

Overview
----------

OpenCanary is a daemon that runs several canary versions of services that alerts when a service is (ab)used.

先安装web服务端
----------------
https://github.com/p1r06u3/opencanary_web


安装系统依赖
----------------
这里推荐使用Centos7或Ubuntu16，因为系统比较新默认python环境为2.7.x，类库也比较新。

Centos7
```
yum -y install libpcap-devel openssl-devel libffi-devel
```

Ubuntu16
```
sudo apt-get install -y python-dev python-pip python-virtualenv libpcap-dev
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
```



安装python依赖
----------------
```
pip install --upgrade pip
pip install pyasn1-modules
pip install service_identity
pip install scapy pcapy
pip install rdpy
pip install pyinotify
pip install apscheduler
```

安装opencanary客户端
----------

```
cd /usr/local/src/
git clone https://github.com/p1r06u3/opencanary.git
cd opencanary/
```

vi opencanary/data/settings.json
将第69行，server.ip改成自己web服务端的ip

```
python setup.py sdist
cd dist
pip install opencanary-0.3.2.tar.gz
```

启动和停止opencanary
----------------------

若第一次安装opencanary，需要先运行opencanaryd --copyconfig，会生成/root/.opencanary.conf配置文件。

启动命令: opencanaryd --start
停止命令: opencanaryd --stop

opencanary日志: /var/tmp/opencanary.log