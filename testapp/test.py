from bs4 import BeautifulSoup
import requests
url="https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@mithileshpandey_48083"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")
print(soup)