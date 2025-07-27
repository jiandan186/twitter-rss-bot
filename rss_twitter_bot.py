
import feedparser
import time
import requests

WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a53f9c4d-d712-4875-b34c-5f710de0fdfb"
TWITTER_RSS_URLS = [
    "https://nitter.net/JohnsonEmm66/rss",
]

seen_entries = set()

def send_to_wechat(text):
    data = {"msgtype": "text", "text": {"content": text}}
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print("推送失败:", e)

def check_feeds():
    global seen_entries
    for url in TWITTER_RSS_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if entry.id not in seen_entries:
                seen_entries.add(entry.id)
                send_to_wechat(f"{entry.title}\n{entry.link}")

if __name__ == "__main__":
    while True:
        check_feeds()
        time.sleep(60)
