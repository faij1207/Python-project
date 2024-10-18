api_key ="c8b922f9e4e3eb1bf2a778a976701b67"
city=input("input city name = ")
import requests
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response=requests.get(url)
data=response.json()
print(data['weather'][0]['description']) 
print(int(data["main"]["temp"]-273),"degree celsius")
