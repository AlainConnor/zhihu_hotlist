import datetime
import requests

url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true"
headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}


now_time = datetime.datetime.now()
year = now_time.year
month = now_time.month
day = now_time.day
hour = now_time.hour


sess = requests.Session()
res = sess.get(url, headers=headers)
data = res.json()["data"]
#print(data)
hot_list = []
for item in data:
    item_id = item["target"]["id"]
    item_title = item["target"]["title"]
    hot_list.append("{}: {}".format(item_id, item_title))

output = "\n".join(hot_list)
with open("./hotlist/{}_{}_{}_{}.txt".format(year, month, day, hour), mode="w") as f:
    f.write(output)
