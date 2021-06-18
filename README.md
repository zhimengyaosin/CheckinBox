# CheckinBox
<details>
  <summary>目前已开发功能(不保证一定可用，随缘修)</summary>

- [天翼云盘每日签到一次，抽奖2次](https://github.com/mengshouer/CheckinBox/tree/master/Cloud189Checkin)

- [最终幻想14积分商城签到](https://github.com/mengshouer/CheckinBox/tree/master/FF14Checkin)

- [什么值得买网页每日签到](https://github.com/mengshouer/CheckinBox/tree/master/smzdmCheckin)

- [52pojie每日签到+免费评分](https://github.com/mengshouer/CheckinBox/tree/master/Checkin52pj)

- [网易云音乐每日签到与刷歌单](https://github.com/mengshouer/CheckinBox/tree/master/NetEase_Music_daily)

- [有道云笔记签到](https://github.com/mengshouer/CheckinBox/tree/master/NoteyoudaoCheckin)

- [V2EX签到](https://github.com/mengshouer/CheckinBox/tree/master/V2EX)

- [恩山论坛签到](https://github.com/mengshouer/CheckinBox/tree/master/Enshan)

- [智友邦签到](https://github.com/mengshouer/CheckinBox/tree/master/Zhiyou)

</details>

<details>
  <summary>运行方式其一</summary>

~~Github Actions版本~~

自行探索

</details>

### [腾讯云函数SCF](https://console.cloud.tencent.com/scf/index)的版本<br>
### SCF计费问题：如果不是大量跑脚本的话，达不到收费标准的，如果不放心的话可以查询[账单详细](https://console.cloud.tencent.com/expense/bill/summary?businessCode=p_scf)<br>
### 实际从账户扣费时按2位小数进行扣费（即扣到分）,账单详细可以看到8位小数<br>
1.下载[requirements.zip](https://github.com/mengshouer/CheckinBox/releases)所需库，到[层](https://console.cloud.tencent.com/scf/layer)里面新建一个层<br>
2.到[函数服务](https://console.cloud.tencent.com/scf/list)里面新建一个函数，输入名字，运行环境选择python3.6，选择空白模板，下一步<br>
3.修改执行方法为index.函数入口(具体到各脚本中看)，修改index.py文件，把SCF版py文件内容覆盖掉里面的函数，删除config.json<br>
4.高级设置，添加多个环境变量key内输入：1.username 2.password 3.推送服务设置值(可选)<br>
value内输入：1.登录手机号 2.登录密码 3.推送服务设置值(可选)<br>
5.层配置，添加层，选择刚才新建的层。最后点完成<br>
6.进入函数→触发管理→新建触发器，按自己需求定时启动<br>
7.自己酌情修改函数的内存与执行超时时间以及其他参数

<details>
  <summary>多账号设置</summary>

Github Actions版本直接Secrets内多账号时账号密码一行一个一一对应<br>
腾讯云函数SCF在每个账号和密码后面添加\n，账号密码也是一一对应<br>
无多Server酱推送<br>

</details>

<details>
  <summary>报错提醒提示</summary>

推送可以设置的参数( Key/name(名称) --> Value(值) )：<br>
Github Actions添加在Setting→Secrets→New secrets，腾讯云函数SCF设置在环境变量里<br>
1. Key: SCKEY --> Value: [Server酱的推送SCKEY的值](http://sc.ftqq.com/)<br>
2. Key: SCTKEY --> Value: [Server酱·Turbo版的推送SCTKEY的值](http://sct.ftqq.com/)<br>
3. Key: Skey --> Value: [酷推调用代码Skey](https://cp.xuthus.cc/)<br>
4. Key: Smode --> Value: 酷推的推送渠道，不设置默认send.可选参数(send,group,psend,pgroup,wx,tg,ww,ding)<br>
5. Key: pushplus_token --> Value: [pushplus推送token](http://www.pushplus.plus/)<br>
6. Key: pushplus_topic --> Value: pushplus一对多推送需要的"群组编码"，一对一推送不用管填了报错<br>
7. Key: tg_token --> Value: Telegram bot的Token，Telegram机器人通知推送必填项<br>
8. Key: tg_chatid --> Value: 接收通知消息的Telegram用户的id，Telegram机器人通知推送必填项<br>
9. Key: tg_api_host --> Value: Telegram api自建的反向代理地址(不懂忽略此项)，默认tg官方api=api.telegram.org<br>
PS:腾讯云函数SCF的默认无推送，需要推送的话需要将[pusher.py](https://github.com/mengshouer/CheckinBox/blob/master/pusher.py)内的内容直接复制到所需函数的代码最上方！！！
#### 一切提醒都是报错提醒，没问题不提醒

</details>

<details>
  <summary>自动同步仓库设置</summary>

基础使用：<br>
> 上游变动后pull插件会自动发起pr，在默认的配置文件中如果有冲突需要自行**手动**确认。<br>

安装[pull插件](https://github.com/apps/pull)，然后设置生效的仓库并确认此项目已在pull插件的作用下<br>
PS. 如果未设置pull.yml配置文件，则mergeMethod的规则默认为none(我也不清楚none的pr规则<br>

高级使用：<br>
> 强制远程分支覆盖自己的分支<br>

1. 先完成基础使用后，在.github目录下(创建/修改)文件pull.yml<br>
2. 参考[插件使用文档](https://github.com/wei/pull#advanced-setup-with-config)进行修改<br>
PS.强制远程分支覆盖自己的分支只需要将mergeMethod的值修改为hardreset

</details>
