from bs4 import BeautifulSoup as bs

file_html = 'sites/site.html'

with open(file_html, 'r', encoding='utf-8') as r:
    for c in r:
        soup = bs(c, 'lxml')
        span = soup.find('span')
        if span != None:
            span = span.text.strip()
            # print(span)
            if 'более' in span:
                print(span)