import requests
from bs4 import BeautifulSoup as bs
import lxml
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait


filenameproduct = 'result/results_product_url4.csv'
HEADERS = {'accept':'*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
URL = 'https://www.wildberries.ru'
chromedrivers = "selen\chromedriver.exe"
FILE_NAMES = 'sites/site.html'
FILE_NAMES2 = 'sites/sites_page/site{}.html'
fail_url_files = 'fail/fail_url.csv'

def get_result(result_name):
    if result_name != None:
        return result_name.text

def find_product_url(url,chromedriver = chromedrivers):
    try:
        brows = Chrome(chromedriver)
        brows.get(url)
        ik = brows.page_source

        try:
            tp1 = brows.find_elements_by_class_name('order-quantity')
            for t in tp1:
                t1 = int(t.find_element_by_tag_name('span').text.strip().replace('более ','').split(' раз')[0].replace(' ',''))
                #print(t1)
                if t1 >= 1000:
                    with open(FILE_NAMES, 'w', encoding='utf8') as f:
                        f.write(ik)
                    get_result_page(url)

        except:
            pass

        brows.quit()
    except:
        with open(fail_url_files,'a',encoding='utf8') as f:
            f.write(url)

    # get_result_page(url)

def get_result_page(url):

    with open(FILE_NAMES, 'r', encoding='utf8') as f:
        soup = bs(f, 'lxml')

        category = soup.find('span', {'class': 'brand'})
        category1 = get_result(category)
        #print(category1)

        category_product = soup.find('span', {'class': 'name'})
        category_product1 = get_result(category_product)
        #print(category_product1)

        img = soup.find('div', {
            'class': 'j-sw-images-carousel swiper-container swiper-container-initialized swiper-container-vertical'}).find_all(
            'li')[1].find('span', {'class': 'slider-content'}).find('img')['src']  # .find('img')['src']
        if img != None:
            img1 = img
         #   print(img1)

        rating = soup.find('div', {'class': 'product-rating'})
        rating1 = get_result(rating).strip()
        #print(rating1)

        tp = soup.find('p', {'class': 'order-quantity j-orders-count-wrapper'})
        if tp != None:
            number_product = tp.find('span').text.strip()
            #print(number_product)
        # number_product = int(tp.find('span').text.strip().replace('более ','').split(' раз')[0].replace(' ',''))

        old_price = soup.find('span', {'class': 'old-price j-final-saving'})
        old_price1 = get_result(old_price).strip()
        #print(old_price1)

        new_price = soup.find('span', {'class': 'final-cost'})
        new_price1 = get_result(new_price).strip()
        #print(new_price1)

        review = soup.find('a', {'id': 'comments_reviews_link'}).find('span')
        review1 = get_result(review).strip()
        #print(review1)

        print(url)
        full_string_results = '{} | {} | {} | {} | {} | {} | {} | {} | {} \n'.format(category1,category_product1,img1,url,rating1,number_product,old_price1,new_price1,review1)
        with open(filenameproduct,'a',encoding='utf8') as f:
            f.write(full_string_results)






def connect(number_file):
    # list_product = []
    # try:
    #     brows = Chrome(chromedriver)
    #     brows.get(url)
    #     ik = brows.page_source
    #     with open(FILE_NAMES2.format(number_file), 'w', encoding='utf8') as f:
    #         f.write(ik)
    #
    #
    #     brows.quit()
    try:
        with open(FILE_NAMES2.format(number_file), 'r', encoding='utf8') as f:
           soup = bs(f,'xml')
           list_tag_a = soup.find_all('a',{'class':'ref_goods_n_p j-open-full-product-card'})
           for a in list_tag_a:
               product_url = URL + a['href']
               #if product_url == 'https://www.wildberries.ru/catalog/15381201/detail.aspx?targetUrl=GP':
                find_product_url(product_url)
                print(FILE_NAMES2.format(number_file))
    except:
        print(number_file)
    # except :
    #     with open(fail_url_files,'a',encoding='utf8') as f:
    #         f.write(url)


    







filename = 'result/results.csv'
# i = 1
for i in range(1,3064):
    connect(i)