import window
from utils import ocr, logger
from MixacLib import cons

import yaml
import codecs
import os
import traceback

__DEFAULT_CONFIG__ = "# OCR语言\n" \
                     "# ch_sim - 中文\n" \
                     "# ja - 日语\n" \
                     "# en - 英语\n" \
                     "# 更多见：https://pic1.zhimg.com/80/v2-6b94055490da0821210d01fe5116facc_720w.jpg\n" \
                     "ocr-lang: ja\n" \
                     "# 支持以下接口：\n" \
                     "# baidu - 百度翻译\n" \
                     "# youdao - 有道智云" \
                     "translator: baidu\n" \
                     "\n" \
                     "# 翻译API APPID\n" \
                     "appid: APPID_HERE\n" \
                     "# 翻译API Key\n" \
                     "key: API_KEY_HERE"
__VERSION__ = "v0.2.0"
__BRANCH__ = "Master"
__REPO__ = "https://github.com/AFterNode/O2T-Translator"

if __name__ == "__main__":
    try:
        cons.console_title("AFterNode O2T Translator")
        print("==========AFterNode O2T Translator==========")
        print("Version: " + __VERSION__)
        print("Branch: " + __BRANCH__)
        print("Repo: " + __REPO__)

        print("Loading configuration file...")
        # 检测配置是否存在，不存在则写入默认配置
        if not os.path.isfile("settings.yml"):
            codecs.open("settings.yml", "w").write(__DEFAULT_CONFIG__)
            print("Configuration file not found, generated a new.")
            print("O2T generated a new configuration file, please check it and run again")
            print("File name: settings.yml")

        settings = yaml.load(codecs.open("settings.yml", "r"), yaml.FullLoader)
        print("____________________")
        print("O2T Translator Options")
        print("OCR Language: " + settings["ocr-lang"])
        print("Translator: " + settings["translator"])
        print("____________________")

        # 载入EasyOCR到内存
        print("Loading OCR...")
        ocr_reader = ocr.make_reader(settings['ocr-lang'])

        # 启动主窗口
        print("Starting main window...")
        window.run(ocr_reader, settings)
    except Exception as e:
        print("Exception occurred, please commit an issue or send it to: h3xadecimal@afternode.cn")
        print(str(e))
        traceback.print_exc()
