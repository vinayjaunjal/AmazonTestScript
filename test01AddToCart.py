from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Navigating to Amazon India
driver.get("https://www.amazon.in")

# Searching for "iphone"
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("iphone")
search_box.submit()

# Selecting the first product from the search results
first_product = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//img[@alt='Sponsored Ad - Apple iPhone 13 (128GB) - Pink']")))
first_product.click()

# Getting the price from the product details page
price_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='52,999']")))
price = price_element.text
print("Price of the product:", price)

# # Adding the product to the cart
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "add-to-cart-button")))
add_to_cart_button.click()

# Closing the browser window
driver.quit()
