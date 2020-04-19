
import urllib.request

r = urllib.request.urlopen('http://www.baidu.com')

r = r.read().decode('utf8').replace('\n', '\r\n')

print(r)

f = open('response.txt', 'a+', encoding='utf-8')

f.write(r)

f.close()

