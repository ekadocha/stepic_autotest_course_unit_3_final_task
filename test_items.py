import time

def test_btn_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, 'Нет ни одной кнопки добавления товара в корзину'