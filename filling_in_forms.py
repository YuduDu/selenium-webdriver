from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.google.com")
Signin = driver.find_element_by_id("gb_70")
Signin.click()
createAccount = driver.find_element_by_xpath("//a[@href='https://accounts.google.com/SignUp?continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&hl=en']")
createAccount.click()
firstname=driver.find_element_by_id("FirstName")
firstname.send_keys("hehe")
#gender = driver.find_element_by_id("Gender")
#all_options = gender.find_element_by_tag_name("option")
#for option in all_options:
#	print ("Value is %s" % option.get_attribute("value")) 
#	option.click
driver.close()
