
from bs4.dammit import EncodingDetector # определеение кодировки
from newspaper import Article
import urllib.request
from bs4 import BeautifulSoup

URL = ["https://nia.eco/category/russia/page/","https://kronoki.ru/ru/news/newswire/?PAGEN_1=","https://prozapovednik.ru/novosti-zapovednikov/page/","http://www.antiatom.ru/page/","https://www.mnr.gov.ru/press/news/?PAGEN_2=", "https://kamtoday.ru/news/ecologics/?PAGEN_1=","https://ecoportal.su/news.html?p=", "https://kronoki.ru/ru/news/newswire/?PAGEN_1="]

for url in URL:
    page =1 
    parser = 'html.parser'
    while True:
     
     user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
     headers={'User-Agent':user_agent,}   

     request=urllib.request.Request(url+str(page),None,headers) 
     response = urllib.request.urlopen(request).read()
     soup = BeautifulSoup(response, parser)

     links=[]
     for link in soup.find_all('a', href=True):
    
      l=link.get('href')
      links.append(l)
     page+=1 
     if (len(links)):   
      for link in links:
        try:
            article = Article(link)
            article.download()
            article.parse()
            # if "Кроноцкий заповедник" in article.text or "заповедник" in article.text or "заповеднике" in article.text or "заповеднику" in article.text or "Камчатка" in article.text or "Камчатке" in article.text or "Камчатку" in article.text or "Камчатки" in article.text or "Камчатский" in article.text or "заповедник" in article.text or "заповеднике" in article.text or "заповеднику" in article.text or "Камчатка" in article.text or "Камчатке" in article.text or "Камчатку" in article.text or "Камчатки" in article.text or "Камчатский" in article.text or "Камчатка" in article.text or "Камчатке"in article.text or "Камчатку" in article.text or "Камчатки" in article.text or "Камчатский" in article.text or "Камчатка" in article.title or "Кроноцкий заповедник" in article.title or "Камчатка" in article.text or  "Камчатка" in article.text or "Камчатке" in article.text or "Камчатку" in article.text or "Камчатки" in article.text or "Камчатский" in article.text:
            if "Камчат" in article.title or ("Камчат" in article.text) and ("заповед" in article.text or "Заповед" in article.text) or "Кроноцкий заповедник" in article.text or "Кроноцкий заповедник" in article.title:
             print (link)
        except:
          pass 
      
     else:
         break
     
