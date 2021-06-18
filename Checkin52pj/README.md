# Checkin52pj
### 52pojie每日签到<br>
因为登录获取到的cookies时间比较长，就没写自动登录了<br>
PS:目前因为ip容易被风控，所以签到失败的几率有点大，如有需要自行修改运行触发时间。
### 使用方法<br>
Github Actions版本<br>
自行探索<br>
<br>
<br>
[腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
PS.目前腾讯云SCF的ip段大概都被52pj封的差不多了，要用的话还是推荐使用Github Actions版本<br>
1.下载requirements.zip所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.pjCheckin，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数，删除config.json<br>
5.高级设置，添加多个环境变量key内输入：1.cookie_52pj 2.推送服务设置值(可选)<br>
value内输入：1.获取到的cookie 2.Server酱推送SCKEY,报错提醒<br>
如果需要自动免费评分的话,新增一个key填写rate_52pj，value 随便填个1就行(非0都行)<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>

### Cookie获取方法<br>
浏览器打开需要签到的网站并登录，F12打开检查<br>
在 Chrome 浏览器下方的开发工具中单击 Network 标签页(其他浏览器大同小异)<br>
F5刷新当前网站，随便选一个Name里面的网页，在右侧Headers内找到Cookie: xxxxxx，复制xxxx的东西，一般很长一大串<br>
Headers如果没有Cookie就换另一个Name里面的网页，实在看不懂就自行baidu吧.jpg<br>
Cookie过期就必须手动更换，再重复一次获取流程，然后Github到secrets里更新，腾讯云函数就到函数配置中修改环境变量的值
