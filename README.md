# AFterNode O2T Translator
[Gitee](https://gitee.com/afternode/t2o-translator) | 
[Github](https://github.com/AFterNode/O2T-Translator) |
[AFterNode](https://afternode.cn)

### 如何使用
安装 [Python](https://python.org/) 3.8+ 后运行：

```python -m pip install -r requirements.txt```

如需GPU加速，请参考 [此处](https://pytorch.org/get-started/locally/) 安装PyTorch CUDA版本

然后运行Release包中的launcher.exe，会自动检测运行依赖后启动

第一次启动会自动生成配置文件，请在生成后修改配置并重新运行

### 支持的翻译API
[百度翻译](https://api.fanyi.baidu.com)

[有道词典](http://fanyi.youdao.com/openapi)

### 如何更新
由于 VMware InstallBuilder 限制，每次更新需先卸载旧版本

打开配置文件进行备份，然后卸载旧版本安装新版本，替换新版本的配置即可

注意：新版本可能有新增的配置，请勿直接替换全部

220614更新：之后可能会用NSIS替换安装器
