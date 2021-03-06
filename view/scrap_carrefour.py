import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

def seleniumScrap(url, browser, dic):
    # Open url in navigator
    browser.get(url)
    time.sleep(6) # Time lapse test 6 or + seconds
    #browser.implicitly_wait(6)
    # Obtain elements acording to class
    product_name = browser.find_element_by_class_name('vtex-store-components-3-x-productBrand')
    integer = browser.find_element_by_class_name('lyracons-carrefourarg-product-price-1-x-currencyInteger')
    decimal = browser.find_element_by_class_name('lyracons-carrefourarg-product-price-1-x-currencyDecimal')
    fraction = browser.find_element_by_class_name('lyracons-carrefourarg-product-price-1-x-currencyFraction')

    dic[product_name.text] = integer.text + decimal.text + fraction.text


def carr_scrap(links):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    product_price = {}
    # links = ["https://www.carrefour.com.ar/oblea-kit-kat-415-g/p", "https://www.carrefour.com.ar/limpiador-en-crema-cif-original-multiuso-500-ml/p", "https://www.carrefour.com.ar/crema-uat-liviana-vitaminas-la-serenisima-tetra-top-200-cc/p", "https://www.carrefour.com.ar/papas-fritas-mc-cain-tradicional-400-g/p"]

    for url in links:
        seleniumScrap(url,browser,product_price)

    # Close Browser and show dictionary
    browser.quit()
    return product_price
