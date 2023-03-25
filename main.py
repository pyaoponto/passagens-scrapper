from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = uc.Chrome()
driver.get("https://www.melhoresdestinos.com.br/passagens-aereas")
time.sleep(10)
original_window = driver.current_window_handle
close_button = "//button[@title='Close']//*[name()='svg']"
elem = driver.find_element(By.XPATH, "//button[@title='Close']//*[name()='svg']")
element = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, close_button)))
elem.click()
elem = driver.find_element(By.XPATH, "//input[@id='origemCP']")
elem.send_keys("Brasília (BSB)")
elem = driver.find_element(By.XPATH, "//input[@id='destinoCP']")
elem.send_keys("Recife (REC)")
elem = driver.find_element(By.XPATH, "//input[@id='data-ida']")
elem.send_keys("25/03/2023")
elem = driver.find_element(By.XPATH, "//input[@id='data-volta']")
elem.send_keys("14/04/2023")
time.sleep(3)
elem = driver.find_element(By.XPATH, "//input[@value='Pesquisar']")
elem.click()
time.sleep(10)

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all("p", {"class": "item-fare fare-price"})
for p in result:
    print(p.find("span", {"class": "amount price-amount"}).text)
driver.quit()