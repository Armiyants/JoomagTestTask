from selenium import webdriver #importing webdriver from Selenium


def start_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    driver.get(url) # The method will navigate to a page given by the URL. WebDriver will wait until the page has been completely loaded.

    forms_count = get_forms(driver)
    images_count = get_images(driver)

    print("html form elements count with method='get': {}".format(forms_count))
    print("html img tags count: {}".format(images_count))

    driver.quit()


def get_forms(driver):
    forms = driver.find_elements_by_xpath("//form[@method='get']")
    return len(forms)


def get_images(driver):
    images = driver.find_elements_by_xpath("//img")
    return len(images)