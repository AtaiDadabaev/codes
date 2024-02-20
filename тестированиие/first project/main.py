from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://demo-opencart.ru/")

def right():
    return ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()

def _input(driver, type, value, text):
    time.sleep(2)
    if (type == "x"):
        driver.find_element(By.XPATH, value).send_keys(text)
        time.sleep(2)
    elif (type == "lt"):
        driver.find_element(By.LINK_TEXT, value).send_keys(text)
        time.sleep(2)
    elif (type == "css"):
        driver.find_element(By.CSS_SELECTOR, value).send_keys(text)
        time.sleep(2)

def find_click(driver, type, value):
    time.sleep(2)
    if (type == "x"):
        driver.find_element(By.XPATH, value).click()
        time.sleep(2)
    elif (type == "lt"):
        driver.find_element(By.LINK_TEXT, value).click()
        time.sleep(2)
    elif (type == "css"):
        driver.find_element(By.CSS_SELECTOR, value).click()
        time.sleep(2)


def test_first():
    time.sleep(2)
    product = driver.find_element(By.LINK_TEXT,"MacBook")
    product.click()
    time.sleep(2)
    screen = driver.find_element(By.XPATH, "//body/div[@id='product-product']/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]")
    screen.click()
    time.sleep(1)
    right()
    time.sleep(1)
    right()
    time.sleep(1)
    right()
    time.sleep(4)

def test_second():
    time.sleep(2)
    buy_product = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(1) div.product-thumb.transition div.button-group > button:nth-child(1)")
    buy_product.click()
    time.sleep(2)
    basket = driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[3]/div[1]/button[1]")
    basket.click()
    time.sleep(4)

def test_third():
    find_click(driver, "lt", "Компьютеры")
    find_click(driver, "lt", "PC (0)")
    time.sleep(2)

def test_fouth():
    pass

def test_fifth():
    find_click(driver, "x", "//header/div[1]/div[1]/div[2]/div[1]/input[1]")
    _input(driver, "x", "//header/div[1]/div[1]/div[2]/div[1]/input[1]", "pc")
    find_click(driver, "x", "//header/div[1]/div[1]/div[2]/div[1]/span[1]/button[1]")
    time.sleep(4)


test_fifth()
