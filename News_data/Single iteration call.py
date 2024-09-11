from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver=webdriver.Edge()
driver.get("https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAA9EtO1xuGdA4juP8HaHZop4SJQ3uFyBcLGlGyUWEhuao91mcOlxef5gWi5Hxpl6lZkcnrgif8xcoUtGZi8EQzFdTuj6ZeL6UD0xrtU3qHkQKB824VyoHdH_8-g7AGeXg122beqj-irU7lV1wAQcMe-FH5r4OYRpLo6wUy19QpO_")

scroll_down=driver.find_element(By.ID, "scroll-down-btn")
scroll_down.click()

accept_cookies=driver.find_element(by=By.CSS_SELECTOR, value="button.btn.secondary.accept-all[name='agree'][value='agree']")
accept_cookies.click()


link_element=driver.find_element(By.TAG_NAME, "a")
link_element.click()



ticker_box=driver.find_element(By.ID, "ybar-sbq")
ticker_box.send_keys("MPC")


search_button=driver.find_element(By.ID, "ybar-search")
search_button.click()

driver.execute_script("window.scrollTo(0,1400)")
news1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "clamp.yf-1e4au4k"))
)
news1.click()
news1_text=driver.find_element(By.CLASS_NAME, "caas-body").get_attribute("textContent")
