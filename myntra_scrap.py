from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.myntra.com")
time.sleep(2)

assert "Online Shopping for Women, Men, Kids Fashion" in driver.title

search = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'desktop-searchBar'))
)
search.clear()
search.send_keys("shirts for men")
time.sleep(2)
search.send_keys(Keys.RETURN)


elems = driver.find_elements(By.CLASS_NAME, 'product-base')
print(f"{len(elems)} items found")
time.sleep(4)

for i in elems:
    print(i.text)




