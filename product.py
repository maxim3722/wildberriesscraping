import requests
from bs4 import BeautifulSoup as bs
import lxml


URL = 'https://www.wildberries.ru/catalog/10394760/detail.aspx?targetUrl=GP'

HEADERS = {'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

session = requests.Session()

request = session.get(URL,headers=HEADERS)
i = 0
if request.status_code == 200:
    soup = bs(request.content,'html5lib')
    div = soup.find('div',{'class':'second-horizontal'}).find_all('span')
    print(div)