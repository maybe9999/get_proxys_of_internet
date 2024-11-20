import requests, json

headers = {

}

def get_proxys_count(proxytype, url):
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = json.loads(r.text)
            return data["total"]
    except Exception as e:
        print("Error obteniendo proxy count")
    
