import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get("https://google.com/")
search = driver.find_element_by_name('q')
search.send_keys("צומת ספרים")
search.submit()

driver.find_element_by_partial_link_text('https://www.booknet.co.il').click()

# get categories
driver.find_element_by_id("nav-icon2").click()

# get sales categories
click_sale = driver.find_element_by_id("top-categories") \
    .find_element_by_xpath("//ul[@id='top-categories']//li[@data-id='250']")

click_category = driver.find_element_by_id("sub-categories-container"). \
    find_element_by_class_name("sub-categories-inner-1").find_element_by_class_name("sub-cat-title"). \
    find_element_by_xpath("//a[@href='/מבצעים/%d7%94%d7%a2%d7%a9%d7%99%d7%a8%d7%99%d7%94-%d7%94%d7%a4%d7%95%d7%aa%d7"
                          "%97%d7%aa']")

action = ActionChains(driver)
action.move_to_element(click_sale).move_to_element(click_category).click().perform()

# select book #1
driver.find_element_by_xpath("//div[@data-fullname='להשאיר אותך מתה']"
                             "//a[@class='btn cart-btn2 blue']").click()

time.sleep(1)  # sleep for 3 seconds
driver.find_element_by_xpath("//button[@class='link-button oprs']").click()

# # select book #2
driver.find_element_by_xpath("//div[@data-fullname='מיינדפולנס בעשר דקות']"
                             "//a[@class='btn cart-btn2 blue']").click()

time.sleep(1)  # sleep for 3 seconds
driver.find_element_by_xpath("//button[@class='link-button oprs']").click()

# click on the basket icon
driver.find_element_by_class_name("cartlink").click()

# enter the purchased list screen
driver.find_element_by_xpath("//a[@href='https://www.booknet.co.il/סל-קניות']").click()

# Choose the shipping method
driver.find_element_by_xpath("//select[@id='shipment']//option[@value='2']").click()

# Filling in the required fields
enter_mail = driver.find_element_by_xpath("//input[@autocomplete='new-password']")
enter_mail.send_keys("yosi_israeli@gmail.com")

enter_first_name = driver.find_element_by_id("customerFirstName")
enter_first_name.send_keys("Yosi")

enter_last_name = driver.find_element_by_id("customerLastName")
enter_last_name.send_keys("Israeli")

enter_mobile_number = driver.find_element_by_id("phone")
enter_mobile_number.send_keys("0501234567")

# mark the checkmark
time.sleep(1)
checkboxes = driver.find_elements_by_class_name("checkbox")
checkboxes[1].click()

# Go to the payment page
driver.find_element_by_id("form-submit-button").click()

# back to the main page
driver.get('https://www.booknet.co.il')

# searching for the specific book
search = driver.find_element_by_name('q')
search.send_keys("מעשה בחמישה בלונים")
search.submit()

# Add to the basket
driver.find_element_by_xpath("//div[@data-fullname='מעשה בחמישה בלונים']"
                             "//a[@class='btn cart-btn2 blue']").click()

time.sleep(1)  # sleep for 3 seconds
driver.find_element_by_xpath("//button[@class='link-button oprs']").click()

# click on the basket icon
driver.find_element_by_class_name("cartlink").click()

# enter the purchased list screen
driver.find_element_by_xpath("//a[@href='https://www.booknet.co.il/סל-קניות']").click()

# close browser
driver.quit()
