import requests


def response_time(host):
    response = requests.head(host)
    if response.status_code == 200:
        return response.elapsed.total_seconds()*1000
    else:
        miss = "did not return 200 OK"
        print(response.status_code)
        return miss

# v1/marketは get method以外は405


def response_time_get(host):
    response = requests.get(host)
    if response.status_code == 200:
        return response.elapsed.total_seconds()*1000
    else:
        miss = "did not return 200 OK"
        print(response.status_code)
        return miss


to_com = response_time("https://api.bitflyer.com")
print(to_com)
to_jp = response_time("https://api.bitflyer.jp")
print(to_jp)

to_com_market = response_time_get("https://api.bitflyer.com/v1/markets")
print(to_com_market)
to_jp_market = response_time_get("https://api.bitflyer.jp/v1/markets")
print(to_jp_market)
