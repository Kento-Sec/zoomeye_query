# zoomeye_query

这个项目已经重构了，增加了一个核心功能以及增强代码的健壮性，也是因此新版不方便更新出来，但这个版本还能用。将计划使用golang来重新实现，到时候会放出来并增加其他的功能。

调用zoomeye开放的api接口进行查询

使用之前python环境需要安装zoomeye：


sudo pip3 install zoomeye

使用方法：

python zoomeye_query.py

*注意：使用前需要在脚本的第8、9行添加zoomeye账户及密码（因此不建议把脚本放到vps上，或者可以注册一个新的账户，但同样存在手机号码会被泄露的风险）

self.username = ""

self.password = ""

普通会员，最多能查询到10000个结果

高级会员30000个

VIP会员40000个
