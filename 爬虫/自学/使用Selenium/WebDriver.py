from selenium import webdriver
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
print(driver.page_source)