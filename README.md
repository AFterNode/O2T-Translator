# AFterNode O2T Translator
### 如何使用
安装 [Python](https://python.org/) 3.8+ 后运行```python -m pip install -r requirements.txt```

如需GPU加速，请参考 [此处](https://pytorch.org/get-started/locally/) 安装PyTorch CUDA版本

然后运行Release包中的launcher.exe，会自动检测运行依赖后启动

第一次启动会自动生成配置文件，目前仅支持百度翻译，请 [开通服务](https://api.fanyi.baidu.com/) 后修改 settings.yml 中的 appid 和 key
