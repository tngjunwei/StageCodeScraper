import requests
import os
import urllib
import json

base_url = "sth" # redacted

def check_stage_number(code: str, ceremony: str ="19") -> bool:
    URL = f"{base_url}/api/events/{ceremony}/stageno/"
    res = requests.get(f"{URL}{code}")
    if res.status_code // 100 != 2:
        return False
    parsed_json = json.loads(res.content)
    return parsed_json["exists"]

def get_filenames(code, ceremony="19"):
    URL = f"{base_url}/api/previewPhotos/{ceremony}/"
    res = requests.get(f"{URL}{code}")
    if res.status_code // 100 != 2:
        return []
    parsed_json = json.loads(res.content)
    return parsed_json["fileNames"]

def save_images(code, filenames, ceremony="19"):
    URL = f"{base_url}/public/preview/{ceremony}/"
    if not filenames:
        return
    
    if not os.path.exists(f"./{code}"):
        os.mkdir(f"./{code}")

    for i, filename in enumerate(filenames):
        urllib.request.urlretrieve(f"{URL}{filename}", f"./{code}/file_{i}.png")
    return