#Selenium WebDriver   
   
           
           
##导航
	driver = get("http://www.google.com")
---------------------
	
###页面交互
打开一个页面后，我们真正需要做的是与页面进行交互，更直白的说是与html页面中的各个元素进行交互，所以首先需要对想进行交互的元素进行选择，webdriver提供了find_element_by_*的方式来对元素进行选择。   
假设我们需要选择下面这个输入框：   

	<input type="text" name="passwd" id="passwd-id" />     
可以选择如下方式：

	inputbox = driver.find_element_by_id("passwd-id")
	inputbox = driver.find_element_by_name("passwd")
	