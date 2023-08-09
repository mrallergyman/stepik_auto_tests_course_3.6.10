from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_cart_button_exist(browser):
    browser.get(link)
    button = len(browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"))
    assert button > 0, "Не нашел кнопку"
    time.sleep(2)
