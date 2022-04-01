import requests

url = "https://www.ceneo.pl/101052360#tab=reviews"
response = requests.get(url)
print(response.status_code)