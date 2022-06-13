import requests
import uuid
import hashlib
import datetime
import pytz

def translate(appid: str, key: str, content: str):
    q = content
    appKey = appid
    salt = uuid.uuid4()
    if len(content) > 20:
        sign = content[0:10] + str(len(q)) + content[len(content)-10:]
    else:
        sign = content

    dt = datetime.datetime.now(tz=pytz.utc)

    params = {
        "q": q,
        "from": "auto",
        "to": "auto",
        "appKey": appKey,
        "salt": salt,
        "sign": sign,
        "curtime": dt
    }

    resp = requests.request("GET", "https://openapi.youdao.com/api", params=params)
    return resp

def analyse(result: dict):
    if result['errorCode'] != 0:
        print("[Translator] Unable to get translation")
        return "翻译失败"
    return result.get("translation")[0]


if __name__ == "__main__":
    s = "1145141919810"
    print("1145141919810"[len(s)-10:])
