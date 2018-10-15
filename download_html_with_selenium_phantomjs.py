from selenium import webdriver

#permission Chromedriver folder by "sudo chmod -R 775 chromedriver_linux64"
driver = webdriver.PhantomJS(executable_path = r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

driver.get('https://spark.apache.org/')

html_document = driver.page_source

print(html_document)