from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5km84u9k2k_e&adgrpid=155259813113&hvpone=&hvptwo=&hvadid=674842289479&hvpos=&hvnetw=g&hvrand=15016406658608587051&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061708&hvtargid=kwd-304880464215&hydadcr=14450_2316420&gad_source=1")
time.sleep(2)

assert "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" in driver.title

search = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'twotabsearchtextbox'))
)
search.clear()
search.send_keys("laptop")
time.sleep(2)
search.send_keys(Keys.RETURN)
# print('done')


elem = driver.find_element(By.CLASS_NAME, 'puis-card-container')
print(elem.text)
time.sleep(4)
add_to_cart = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'a-autoid-1-announce'))
)
add_to_cart.click()
time.sleep(4)
# print('done')


go_to_cart = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'a-button-text'))
)
go_to_cart.click()
time.sleep(4)
# print('done')


proceed_to_buy = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.NAME, 'proceedToRetailCheckout'))
)
proceed_to_buy.click()
time.sleep(4)
# print('done')


driver.close()




