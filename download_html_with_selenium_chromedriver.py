from selenium import webdriver

#permission Chromedriver folder by "sudo chmod -R 775 chromedriver_linux64"
driver = webdriver.Chrome(executable_path = r'/home/akash/web_scraping/chromedriver_linux64/chromedriver')

driver.get('https://spark.apache.org/')

html_document = driver.page_source

print(html_document)