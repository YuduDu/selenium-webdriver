import unittest
from selenium import webdriver

class test(unittest.TestCase):

	@classmethod
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_title(self):
		self.driver.get("http://www.aweber.com")
		self.assertEqual(
			self.driver.title,
			'AWeber Email Marketing Services & Software Solutions for Small Business')
	
