from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as bs
import lxml

# chromedriver = "selen\chromedriver.exe"  #C:/chromedriver_win321/
#
# find_url = 'https://www.wildberries.ru/catalog/10394760/detail.aspx?targetUrl=GP'
# # time.sleep(10)
# brows = Chrome(chromedriver)
# brows.get(find_url)
# element = WebDriverWait(brows, 10)
# # time.sleep(15)
# ik = brows.page_source
# brows.quit()
#
# filename = 'sites/site.html'
# with open(filename,'w',encoding='utf8') as f:
#     f.write(ik)
filename = 'sites/site.html'

def get_result(result_name):
    if result_name != None:
        return result_name.text

with open(filename,'r',encoding='utf8') as f:
    soup = bs(f,'lxml')

    category = soup.find('span',{'class':'brand'})
    category = get_result(category)
    print(category)

    category_product = soup.find('span', {'class': 'name'})
    category_product = get_result(category_product)
    print(category_product)

    img = soup.find('div',{'class':'j-sw-images-carousel swiper-container swiper-container-initialized swiper-container-vertical'}).find_all('li')[1].find('span',{'class':'slider-content'}).find('img')['src']#.find('img')['src']
    if img != None:
        print(img)

    rating = soup.find('div',{'class':'product-rating'})
    rating = get_result(rating).strip()
    print(rating)

    tp = soup.find('p', {'class': 'order-quantity j-orders-count-wrapper'})
    if tp != None:
        number_product = tp.find('span').text.strip()
        print(number_product)
    # number_product = int(tp.find('span').text.strip().replace('более ','').split(' раз')[0].replace(' ',''))

    old_price = soup.find('span',{'class':'old-price j-final-saving'})
    old_price = get_result(old_price).strip()
    print(old_price)

    new_price = soup.find('span',{'class':'final-cost'})
    new_price = get_result(new_price).strip()
    print(new_price)

    review = soup.find('a',{'id':'comments_reviews_link'}).find('span')
    review = get_result(review).strip()
    print(review)



# tag_p = brows.find_elements_by_class_name('order-quantity')
# for p in tag_p:
#     t = p.find_element_by_tag_name('span').text
#     print(t)
# tag_name = brows.find_elements_by_class_name('brand')
# for t_n in tag_name:
#     name = t_n.text
#     print(name)
# tag_name_category = brows.find_elements_by_class_name('name')
# for t_n in tag_name_category:
#     name_category = t_n.text
#     print(name_category)
#
# tag_img_category = brows.find_elements_by_class_name('slider-content')
# for t_n in tag_name_category:
#     name_category = t_n.find_elements_by_tag_name('img')
#     for img in name_category:
#         print(img['src'])
#
#
#
#
# brows.quit()


# i +=12
