## V2EX 西安群聊状态监控页面

如果群状态异常了，各位群管请发一个 PR 修改在 `config.json` 里面的相关信息：

```json
{
    "groupAdminQR": "https://u.wechat.com/kMVn7TVrrkF359yKlmUnWFY",  // 群管理的联系方式
    "backupGroupQR": "https://weixin.qq.com/g/xxxxx",  // 备份群的二维码链接
    "mainGroupStatus": "normal",  // "nomal" 或者 "abnormal" 表示主群状态正常或是不正常
    "backupGroupStatus": "normal",  // "normal" 或者 "full" 表示备份群是否已达 200 人上限
    "lastUpdated": "2024-12-31"  // 最后一次状态更新时间
}
```

希望大家聊的开心。
