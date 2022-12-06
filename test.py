import requests

x = requests.get('https://www.op.gg/summoners/na/Best%20URGOT%20in%20NA', 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})

print(x.text)