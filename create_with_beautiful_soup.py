from selenium import webdriver
from bs4 import BeautifulSoup

#permission PhantomJS folder by "sudo chmod -R 775 PhantomJS"
driver = webdriver.PhantomJS(executable_path = r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get('https://spark.apache.org/')

html_document = driver.page_source

soup = BeautifulSoup(html_document, 'lxml')

print(soup.prettify())

driver.quit()