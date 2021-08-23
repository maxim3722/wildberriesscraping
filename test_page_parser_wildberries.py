import requests
from bs4 import BeautifulSoup as bs
import lxml


URL = 'https://www.wildberries.ru/catalog/sport/vidy-sporta/fitnes/yoga'

HEADERS = {'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

session = requests.Session()

request = session.get(URL,headers=HEADERS)
i = 0
if request.status_code == 200:
    soup = bs(request.content,'xml')
    list_tag_a = soup.find_all('a',{'class':'ref_goods_n_p j-open-full-product-card'})
    for a in list_tag_a:
        print(a['href'])
        # category = a.find('span',{'class':'goods-name c-text-sm'})
        # product = a.find('strong',{'class':'brand-name c-text-sm'})
        # image = a.find_all('img',{'class':'thumbnail'})[1]['src']
        # raiting = a.find('span',{'itemprop':'aggregateRating'})
        # # number_of_sales_transfer = 0
        # price_no_discont = str(a.find('span',{'class':'price-old-block'})).split('del')
        # if len(price_no_discont)>2:
        #     print(price_no_discont[1].replace('>','').split('<')[0])
        # price_discont = a.find('ins',{'class':'lower-price'})
        # quantity_reviews = a.find('span',{'class':'dtList-comments-count c-text-sm'})
        # print(category.text)
        # print(product.text)
        # print(image)
        # print(raiting)
        # if len(price_no_discont)>2:
        #     price_no_discont = price_no_discont[1].replace('>','').split('<')[0]
        #     print(price_no_discont)
        # print(price_discont)
        # print(quantity_reviews)
        # i += 1
        # print(i)
