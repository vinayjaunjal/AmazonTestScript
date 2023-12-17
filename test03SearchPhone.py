from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Amazon.in
driver.get("https://www.amazon.in")

# Find the search bar and enter "phone"
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("phone", Keys.ENTER)

# Wait for the search results to load
time.sleep(5)

# Apply filters by brand "Samsung"
brand_filter = driver.find_element(By.XPATH, "//span[text()='Samsung']")
brand_filter.click()

# Wait for the filtered results to load
time.sleep(5)

# Capture the filtered list for validation
filtered_items = driver.find_elements(By.CSS_SELECTOR, ".s-result-list .s-result-item")

# Close the browser
driver.quit()

# Validate the number of filtered items
num_filtered_items = len(filtered_items)
print("Number of filtered items:", num_filtered_items)



