from bs4 import BeautifulSoup

soup = BeautifulSoup(open('table.html'), 'lxml')

#print(soup.prettify())

for tr in soup.find_all('tr'):
    #print(tr.text)
    for td in tr.find_all('td'):
        print(td.text)

