import requests
from bs4 import BeautifulSoup

Url = 'https://auto.am/search/passenger-cars?q={%22category%22:%221%22,%22page%22:%221%22,%22sort%22:%22latest%22,%22layout%22:%22list%22,%22user%22:{%22dealer%22:%220%22,%22id%22:%22%22},%22make%22:[%22246%22],%22model%22:{%22246%22:[%223082%22]},%22year%22:{%22gt%22:%221911%22,%22lt%22:%222022%22},%22usdprice%22:{%22gt%22:%220%22,%22lt%22:%22100000000%22},%22mileage%22:{%22gt%22:%2210%22,%22lt%22:%221000000%22}}'

Headers = {"user-agent":"Mozilla/5.0 (X11; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

Host = 'https://auto.am'

def get_html(url,params=None):
    r = requests.get(url,headers=Headers,params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all("div",class_="card")
    cars = []
    for item in items:
        s = item.find("span",class_="card-title bold").get_text(strip=True)
        asd = Host+item.find("a").get("href")
        gin = item.find("span",class_="").get_text(strip=True)
        cars.append({"title":s,"link":asd,"price":gin})
    for el in cars:
        print(el)

def parse():
    html = get_html(Url)
    if html.status_code==200:
        get_content(html.text)
    else:
        print("error")

parse()
