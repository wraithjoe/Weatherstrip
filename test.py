import requests

r = requests.get('http://forecast.weather.gov/MapClick.php?lat=32.94138102241732&lon=-96.73141942726403#.WNcujPnytPY')
print(r.text)