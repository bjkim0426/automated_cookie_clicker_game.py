import time
from time import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


URL = 'https://orteil.dashnet.org/cookieclicker/'

chrome_driver_path = '/Users/peter/Desktop/HTML/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)
driver.implicitly_wait(10)

select_language_element = driver.find_element(By.ID, value='langSelect-EN')
select_language_element.click()

cookie_element = driver.find_element(By.ID, value='bigCookie')

cursor_item_price_element = driver.find_element(By.ID, value='productPrice0')
cursor_price = int(cursor_item_price_element.text)
cursor_item_click_element = driver.find_element(By.ID, value='product0')

grandma_item_price_element = driver.find_element(By.ID, value='productPrice1')
grandma_price = int(grandma_item_price_element.text)
grandma_item_click_element = driver.find_element(By.ID, value='product1')

seconds = 100000
end = time() + seconds

check = time() + 5

while time() < end:
    # sleep(0.15)
    current_cookie_count = int(driver.find_element(By.ID, value='cookies').text.split()[0])
    cookie_element.click()
    # print(current_cookie_count, time(), check)
    print(current_cookie_count)


    if time() > check:
        try:
            farm_item_price_element = driver.find_element(By.ID, value='productPrice2')
            farm_price = int(farm_item_price_element.text)
            farm_item_click_element = driver.find_element(By.ID, value='product2')
            if current_cookie_count > farm_price:
                farm_item_click_element.click()
        except: ValueError

        if current_cookie_count > grandma_price:
            grandma_item_click_element.click()
        if current_cookie_count > cursor_price:
            cursor_item_click_element.click()

        check = time() + 5



sleep(10000)
#
# farm_item_price_element = driver.find_element(By.ID, value='productPrice2')
# farm_price = int(farm_item_price_element.text)
# farm_item_click_element = driver.find_element(By.ID, value='product2')
#
#
# mine_item_price_element = driver.find_element(By.ID, value='productPrice3')
# mine_price = int(mine_item_price_element.text)
# mine_item_click_element = driver.find_element(By.ID, value='product3')
#
#
#
# factory_item_price_element = driver.find_element(By.Id, value='productPrice4')
# factory_price = int(factory_item_price_element.text)
# factory_item_click_element = driver.find_element(By.ID, value='product4')
#
#
# bank_item_price_element = driver.find_element(By.ID, value='productPrice5')
# bank_price = int(bank_item_price_element.text)
# bank_item_click_element = driver.find_element(By.ID, value='product5')
#
#
# temple_item_price_element = driver.find_element(By.ID, value='productPrice6')
# temple_price = int(temple_item_price_element.text)
# temple_item_click_element = driver.find_element(By.ID, value='product6')
#
# wizard_tower_item_price_element = driver.find_element(By.ID, value='productPrice7')
# wizard_tower_price = int(wizard_tower_item_price_element.text)
# wizard_tower_item_click_element = driver.find_element(By.ID, value='product7')
#
#
# shipment_item_price_element = driver.find_element(By.ID, value='productPrice8')
# shipment_price = int(shipment_item_price_element.text)
# shipment_item_click_element = driver.find_element(By.ID, value='product8')
#
#
# alchemy_lab_item_price_element = driver.find_element(By.ID, value='productPrice9')
# alchemy_lab_price = int(alchemy_lab_item_price_element.text)
# alchemy_lab_item_click_element = driver.find_element(By.ID, value='product9')
#
#
#
# portal_item_price_element = driver.find_element(By.ID, value='productPrice10')
# portal_price = int(portal_item_price_element.text)
# portal_item_click_element = driver.find_element(By.ID, value='product10')
#
#
# time_machine_item_price_element = driver.find_element(By.ID, value='productPrice11')
# time_machine_price = int(time_machine_item_price_element.text)
# time_machine_item_click_element = driver.find_element(By.ID, value='product11')
#
# antim_condenser_item_price_element = driver.find_element(By.ID, value='productPrice12')
# antim_condenser_price = int(antim_condenser_item_price_element.text)
# antim_condenser_item_click_element = driver.find_element(By.ID, value='product12')
#
#
# prism_item_price_element = driver.find_element(By.ID, value='productPrice13')
# prism_price = int(prism_item_price_element.text)
# prism_item_click_element = driver.find_element(By.ID, value='product13')
#
#
#
# chance_maker_item_price_element = driver.find_element(By.ID, value='productPrice14')
# chance_maker_price = int(chance_maker_item_price_element.text)
# chance_maker_click_element = driver.find_element(By.ID, value='product14')
#
#
# fractal_engine_item_price_element = driver.find_element(By.ID, value='productPrice15')
# fractal_engine_price = int(fractal_engine_item_price_element.text)
# fractal_engine_click_element = driver.find_element(By.ID, value='product15')
#
#
# javascript_console_item_price_element = driver.find_element(By.ID, value='productPrice16')
# javascript_console_price = int(javascript_console_item_price_element.text)
# javascript_console_click_element = driver.find_element(By.ID, value='product16')
#
# idleverse_item_price_element = driver.find_element(By.ID, value='productPrice17')
# idleverse_console_price = int(idleverse_item_price_element.text)
# idleverse_click_element = driver.find_element(By.ID, value='product17')
#
#
# cortex_baker_item_price_element = driver.find_element(By.ID, value='productPrice18')
# cortex_baker_price = int(cortex_baker_item_price_element.text)
# cortex_baker_click_element = driver.find_element(By.ID, value='product18')