# IDS-basedSnort

基于snort base mysql 的入侵检测系统

## 大致思路

1. 安装服务启动器 apache
2. 安装数据库 mysql
3. 下载php
4. 以上三步推荐使用Appserv集成度好，不需要动脑子
5. 下载下面链接 <http://101.132.76.180:8000/f/1471665707/>不需要登陆
6. 将snort路径位于c:\snort中 ！！！,不然自己要配置路径，很麻烦
7. 启动appserv 登录localhost 按照pdf修改网页内容，`snort/etc/snort.conf`不要动，修改好的。
8. 可以到使用`c:\snort\bin\snort -i1 -c c:\snort\etc\snort.conf -l c:\snort\log -T`看一下是否有错
9. 主要-i 后面是网卡的索引号，使用到bin目录下的snort -W看下自己的index 一般来讲 看见网卡描述是厂商的名字的就选对应的index,但是此电脑中没有描述，一个个试过来。
10. `c:\snort\bin\snort -i1 -c c:\snort\etc\snort.conf -l c:\snort\log -A fast `可以将记录写入log\alert.ids里面可以看一下
11. `c:\snort\bin\snort -i1 -c c:\snort\etc\snort.conf -l c:\snort\log -dev` 刷新base看入侵尽量

## 常见错误
1. 注意网卡的选择，要输入命令运行snort后，alert.ids没东西，大多数就是网卡有错。
2. debug的时候可以只保留一个规则，如local.rules 
`alert icmp any any -> $HOME_NET any (msg:"SNORT：any host ping this host";sid:201900003; rev:1;)`看base是不是有icmp的alert
# 都2022年了，还在用十多年前的项目来用作当前的IDS，整笑了。😜😜
# 如果上述进不去了就用
<https://cloud.189.cn/web/share?code=VVNvemyiaaEf>（访问码：zqr7）
