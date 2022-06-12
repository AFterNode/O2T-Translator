import requests
import random
import hashlib
import urllib

def translate(appid: str, key: str, content: str):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    print("[Translator] Generating BaiduAPI sign...")
    salt = random.randint(1, 100)
    if not isinstance(str(appid), str):
        print("[Translator] APPID is not an string")
        return "Failed"
    elif not isinstance(content, str):
        print("[Translator] Content is not an string")
        return "Failed"
    elif not isinstance(str(salt), str):
        print("[Translator] Salt is not an string")
        return "Failed"
    elif not isinstance(key, str):
        print("[Translator] Key is not an string")
        return "Failed"
    sign_orig = str(appid) + content + str(salt) + str(key)
    md5 = hashlib.md5()
    md5.update(sign_orig.encode("utf-8"))
    print("[Translator] Generated sign: " + md5.hexdigest())

    dic = {
        "q": content,
        "from": "auto",
        "to": "zh",
        "appid": appid,
        "salt": salt,
        "sign": md5.hexdigest()
    }

    print("[Translator] Sending request...")
    resp = requests.post("https://fanyi-api.baidu.com/api/trans/vip/translate", dic, headers=header)
    print("[Network] Response: ")
    print(resp.json())
    return resp

def analyse_result(result: dict):
    trans_result = result['trans_result'][0]['dst']
    return trans_result
