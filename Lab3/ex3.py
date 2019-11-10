###Exercise 3
import urllib.request
import urllib.error

print("Input a Webpage URL:\n")
url = "https://" + input()
req = urllib.request.Request(url)
try:
    response = urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    if e.code == 404:
        print('Website not found!\nError code: ', e.code)
except urllib.error.URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print("Page is present on a server")