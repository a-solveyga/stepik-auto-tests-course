import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_card_button_is_displayed(browser):
    browser.get(link)
    output1 = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert output1, "Button isn't displayed"
    time.sleep(30)
