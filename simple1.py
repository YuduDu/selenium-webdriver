#basic import
from selenium import webdriver
#import Keys to allow you enter words like on keyboard
from selenium.webdriver.common.keys import Keys

import time

#open a Firefox broswer
driver = webdriver.Firefox()
#open a link, if the page uses a lot of AJAX on load the WebDriver may not know when it has completely loaded, in this case, you can use waits.
driver.get("http://www.google.com")
#set a assert to make sure title contains "Google"
assert "Google" in driver.title
#find input box using its id "lst-ib"
inputbox = driver.find_element_by_id("lst-ib")
#enter something to search, same idea as enter with keyboard
inputbox.send_keys("adsfadfaudsfauysdgfaydgfjahdgfayjdgfajsdyghfa")
#click enter on the keyboard
inputbox.send_keys(Keys.RETURN)
#make sure there return some result
assert "did not match any documents" not in driver.page_source
#close the tab
time.sleep(3)
driver.close()
#driver.quit() - close the broswer, quit all tab