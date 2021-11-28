from selenium import webdriver

driver= webdriver.Edge("C://Users//Aditi//Desktop//msedgedriver.exe")
driver.get("https://hotel.testplanisphere.dev/ja/login.html")
driver.find_element_by_id("email").send_keys("blue@gmail.com")
driver.find_element_by_id("password").send_keys("applebanana")
driver.find_element_by_id("login-button").click()
