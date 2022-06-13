from . import baidu
from . import youdao

TRANSLATOR_LST = ["baidu", "youdao"]

def translate(mode, appid, key, content):
    if mode == "baidu":
        return baidu.translate(appid, key, content)
    elif mode == "youdao":
        return youdao.translate(appid, key, content)

def analyse(mode, result):
    if mode == "baidu":
        return baidu.analyse_result(result)
    elif mode == "youdao":
        return youdao.analyse(result)
