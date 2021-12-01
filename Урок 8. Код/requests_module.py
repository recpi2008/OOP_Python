import requests

r = requests.get('http://learn.python.ru/')
print(r)


image = requests.get('https://learn.python.ru/media/projects/sl1_Cj4bKxp.png')
with open('new_image.png', 'wb') as f:
    f.write(image.content)


# формирование запроса https://github.com/requests/get?key=val
data = {'key1': 'value1'}
resp = requests.get("https://github.com/requests/get", params=data)
print(resp)


# URL, на который собираетесь отправлять запрос
url = 'http://ru.stackoverflow.com/search?q=question'
# Параметры запроса
params = {
    'tag': 'python',
}
# Ответ
r = requests.get(url=url, params=params) # r.url = 'https://ru.stackoverflow.com/search?q=question&tag=python'
print(r)


response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response)
