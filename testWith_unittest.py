#selenium doesn't provide a testing tool/framwork itself. so we can choose python's unittest module as a framework to write testcase.
#Other chooses for test case are py.test and nose
import unittest
from selenium import webdriver
#Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):#the test case class is inherited from unittest.TestCase.
	
	#setUp part is used to initialization. this method will get called first in this class.
	def setUp(self):
		self.driver = webdriver.Firefox()

	
	def test_search_in_python_org(self):# this is the test case method. the test method should always start with characters "test". the first line inside this method need to create a local refernce to the driver object created in setUp method.
		driver = self.driver
		driver.get("http://www.python.org")#WebDriver will wait until the page has fully loaded before returning control to your test or script.
		self.assertIn("Python", driver.title)
		elem = driver.find_element_by_name("q")
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

	#tearDown method will get called after every test method. All cleanup actions will execute in this part.
	def tearDown(self):#
		self.driver.close()

if __name__ == "__main__":
	unittest.main()