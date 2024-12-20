import requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.content)
response.encoding = 'utf-8' # Optional: requests infers this internally
print(response.text)

