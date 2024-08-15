# PixDrop

## 想法💡
你好，我是悦创。

这个项目是一个轻松上传和分享图片的地方。

说个大白话：图床。

市面上已经有成熟的图床项目，我为什么要重复造轮子呢？很简单：我只想直接存储到服务器本地，不想存储到存储桶。

因为存储桶没续费或者想要迁移我的没那么轻松，并且数据没那么轻易的看见。我这人是备份狂魔，喜欢数据存储是看得见的，自己能掌控维护的。

开源项目是成熟，但是不受我掌控并且我不需要太复杂的功能。

## 计划🧾

- [ ] 功能计划
  - [ ] 页面可以粘贴上传图片；
  - [ ] 页面可以拖拽上传图片;
  - [ ] 页面可以点击上传文件夹里面所有图片，在服务器上面创建对应的文件夹和图片，批量生成链接在右侧；「待定」
  - [ ] 页面左侧为上传窗口，右侧显示一组生成的图片链接：
    - [ ] URL
    - [ ] HTML
    - [ ] Markdown
  - [ ] 图片上传成功后，自动复制 Markdown 图片链接；
  - [ ] 上传需要用户登录；
  - [ ] 图片存储到服务器本地；
  - [ ] 可以配置只允许特定域名或 ip 访问；
  - [ ] 需要一个后台查看之前提交过的图片以及链接
- [ ] 设想
  - [ ] 更简单的方法就是在服务器上新建站点
  - [ ] 然后解析域名
  - [ ] 直接建立远程服务器的 .git 仓库
  - [ ] 本地直接推送（手动编写图片链接）
  - [ ] 如果图省事的话，在这个站点开发一个自动读取文件夹内容构建链接即可。
    - [ ] 限制可访问的域名即可