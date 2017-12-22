import urllib
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.de/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiU4pKNv53YAhUNDuwKHWdvBl4Q_AUIDSgE&biw=1277&bih=634' \
        .format('bear')

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

raw_img = soup.find('img')
link = raw_img.get('src')
if link:
    print(link)
    response = urllib.request.urlopen(link)
    data = response.read()
    print(data)
