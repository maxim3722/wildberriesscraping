import requests
from bs4 import BeautifulSoup as bs
import lxml


URL = 'https://www.wildberries.ru/catalog/sport'
STATIC_URL = 'https://www.wildberries.ru'

HEADERS = {'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

session = requests.Session()

def connect(url):
    request = session.get(url, headers=HEADERS)
    if request.status_code == 200:
        return request.content

def get_url_category(url):
    list_category = []
    soup = bs(connect(url),'lxml')
    sport_ul = soup.find('div',{'class':'menu-item-drop-content j-menu-catalog-second-drop'}).find_all('ul')
    # print(len(sport_ul))
    for ul in sport_ul:
        list_tag_li = ul.find_all('li')
        for li in list_tag_li:
            url_category =STATIC_URL +  li.find('a')['href']
            # print(url_category)
            list_category.append(url_category)
    print(len(list_category))
    return list_category


def get_subcategories(list_category):
    list_subcategory = []
    for url in list_category:
        # print(url)
        soup = bs(connect(url), 'lxml')
        list_tag_a = soup.find('li', {'class':'selected hasnochild'}).find_all('a')
        if len(list_tag_a)>1:
            for a in list_tag_a:
                url = STATIC_URL + a['href']
                # print(url)
                list_subcategory.append(url)
    return list_subcategory




# ?page=7
def get_page_url(url):
    list_end_url=[]
    page = '?page='
    o = 0
    i = 1
    while i<200:
        end_url = url+page+str(i)
        soup = bs(connect(end_url), 'lxml')
        div = soup.find('div',{'class':'dtList i-dtList j-card-item'})
        if div !=None:
            print(end_url)
            list_end_url.append(end_url)
        else:
            break
        i+=1
    return list_end_url

def run_parser():
    i = 1
    dict_all_pages = {}
    list_category = get_url_category(URL)
    list_subcategory = get_subcategories(list_category)
    for urls in list_subcategory:
        dict_all_pages[i] = get_page_url(urls)
        i += 1
    file_site = 'result/results.csv'
    for k in dict_all_pages:
        result_str = str(k) + ' : ' + '; '.join(dict_all_pages[k]) + '\n'
        with open(file_site, 'a', encoding='utf-8') as ws:
            ws.write(result_str)
        # print(k,len(dict_all_pages[k]))
    # print(len(list_subcategory))
if __name__ == '__main__':
    run_parser()









