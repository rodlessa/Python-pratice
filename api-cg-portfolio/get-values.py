import requests
coina = "harmony"
a_api= "https://api.coingecko.com/api/v3/simple/price?ids="+coina+"&vs_currencies=,usd&include_24hr_change=true"

h_api = requests.get(a_api)
r = h_api.json()
coin = "Harmony"
print(coin,": $", r['harmony']['usd'],  " changes last 24h: ","%.3f" % r['harmony']['usd_24h_change'],"%")

coinb = "defi-kingdoms"
b_api =  "https://api.coingecko.com/api/v3/simple/price?ids="+coinb+"&vs_currencies=,usd&include_24hr_change=true"

j_api = requests.get(b_api)
jw = j_api.json()
coin_jw = "Jewel"
print(coin_jw,": $", jw['defi-kingdoms']['usd'], " changes last 24h: ","%.3f" % jw['defi-kingdoms']['usd_24h_change'],"%")
