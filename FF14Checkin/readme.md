# FF14Checkin
### 最终幻想14积分商城签到，修改自[FF14AutoSignIn](https://github.com/renchangjiu/FF14AutoSignIn)<br>
### 推荐使用腾讯云函数跑，小  心  异  地  登  录.jpg<br>
### 使用方法<br>
Github Actions版本<br>
1.点击项目右上角的Fork，Fork此项目<br>
2.到自己Fork的项目点击Setting→Secrets→New secrets<br>
3.Name填写login_name，Value填写 登录账号<br>
4.再New secrets一个，Name填写login_password，Value填写 登录密码<br>
5.再New secrets一个，Name填写area_name，Value填写 大区(陆行鸟、猫小胖、莫古力)<br>
6.再New secrets一个，Name填写server_name，Value填写 游戏服务器(神意之地、萌芽池、拉诺西亚……)<br>
7.再New secrets一个，Name填写role_name，Value填写 游戏名(必须完全一致)<br>
8.在"Actions"中的"run"下点击"Run workflow"即可手动执行签到，后续运行按照schedule，默认在每天凌晨0:30自动签到，可自行修改<br>
9.(可选)New secrets，Name填写SCKEY，Value填写 Server酱推送SCKEY  报错提醒用
<br>
<br>
[腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
1.下载requirements.zip所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.go，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数，删除config.json<br>
4.高级设置，添加多个环境变量key内输入：1.login_name 2.login_password 3.area_name 4.server_name 5.role_name 6.SCKEY(选填)<br>
value内输入：1.登录号 2.登录密码 3.大区(陆行鸟、猫小胖、莫古力) 4.游戏服务器(神意之地、萌芽池、拉诺西亚……) 5.游戏名(必须完全一致) 6.Server酱推送SCKEY,报错提醒<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>