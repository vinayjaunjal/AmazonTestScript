from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Amazon.in
driver.get("https://www.amazon.in/")

# Click on Account Button
button1 = driver.find_element(By.XPATH, "//span[normalize-space()='Account & Lists']")
button1.click()

# Click on Create Your Amazon Button
button2 = driver.find_element(By.ID, "createAccountSubmit")
button2.click()

# Fill in registration form details
name_input = driver.find_element(By.ID, "ap_customer_name")
name_input.send_keys("Name123")

email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("name1231@gmail.com")

password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("Pass123")

#Click on Verify Mobile Number Button

button = driver.find_element(By.ID, "continue")
button.click()

# Close the browser
driver.quit()
