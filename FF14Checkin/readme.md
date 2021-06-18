# FF14Checkin
### 最终幻想14积分商城签到，修改自[FF14AutoSignIn](https://github.com/renchangjiu/FF14AutoSignIn)<br>
### 现在在异地IP运行的话会触发验证码，小  心  异  地  登  录.jpg<br>
### 使用方法<br>
Github Actions版本<br>
自行探索<br>
<br>
[腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
1.下载requirements.zip所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.go，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数，删除config.json<br>
4.高级设置，添加多个环境变量key内输入：1.fflogin_name 2.fflogin_password 3.area_name 4.server_name 5.role_name 6.推送服务设置值(可选)<br>
value内输入：1.登录号 2.登录密码 3.大区(陆行鸟、猫小胖、莫古力) 4.游戏服务器(神意之地、萌芽池、拉诺西亚……) 5.游戏名(必须完全一致) 6.推送服务设置值(可选)<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>