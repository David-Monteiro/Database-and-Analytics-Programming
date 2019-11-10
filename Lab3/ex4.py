###Exercise 4
import urllib.request
import urllib.parse
import urllib.error

print("Input a city:\n")
city = input()

url = 'http://api.openweathermap.org/data/2.5/weather?'
query_args = {'q': city}
headers = {'User-Agent': 'Mozilla 5.10'}
data = urllib.parse.urlencode(query_args).encode('ascii')
req = urllib.request.Request(url, data, headers)

try:
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print(html)
except urllib.error.HTTPError as e:
    if hasattr(e, 'code'):
        if int(e.code / 100) == 4:
            print("Client error")
        if int(e.code / 100) == 3:
            print("Server error")
        print(e.code)
else:
    print("Error!")

