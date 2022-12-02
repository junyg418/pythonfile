import threading, requests, time
 
class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self) 
        self.url = url
 
    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print('thr 1')
        time.sleep(1)
        print('thr 2')
        time.sleep(1)
        print('thr 3')
        print(self.url, len(resp.text), ' chars')

t = HtmlGetter('http://google.com')
t.start()
time.sleep(1)
n = HtmlGetter('http://naver.com')
n.start()
print(1)
time.sleep(1)
print(2)
time.sleep(1)
print(3)

print("### End ###")