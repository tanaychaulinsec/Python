import requests
city_name="kolkata"
url='http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
data=requests.get(url+city_name).json()

