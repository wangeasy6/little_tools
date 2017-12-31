# 煲机工具
##### 使用白噪声和粉红噪声自动煲耳机的小工具。

### 说明
* 使用 python 语言，煲机素材使用 白噪声和粉红噪声；
* 使用白噪声煲 20 h；再使用粉红噪声煲 10 h；再播放正常音乐；
* 煲机播放每隔 19m，停 1m；
* 支持断点续煲，中断的时间保存在 time.bak 中。如果想要重新煲机，把这个文件删除即可；
* 可以在相应的素材目录下自己添加歌曲。(格式支持 mp3 wav flac 中文，不支持 ape)

### 环境搭建和运行
1、安装 python， 勾选添加环境变量(python 3.6版本 + Windows)
2、pip install pygame
3、运行： python Burning_Tool.py
4、退出运行：Ctrl + C

### 配置
* playing_time      是播放的单位时间
* pause_time        是停止的时间
* white_noise_time  是白噪声播放的时长
* pink_noise_time   是粉噪声播放的时长
* TEST              是为了配置上面4个参数而设置的一个测试控制变量，为 1 的时候，则使用测试参数
* UPDATE_FOLDER     为 1 则开启实时更新文件夹中的歌曲