from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox()
driver.get("http://engineering.aweber.com/getting-started-with-ui-automated-tests-using-selenium-python/")
search = driver.find_element_by_id('search')
element = driver.find_element_by_xpath("//a[@href='http://engineering.aweber.com/category/apis/']")
element.click()
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element,search).perform()
time.sleep(3)
driver.close()