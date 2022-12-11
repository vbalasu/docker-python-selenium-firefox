def handler(event, context):
    return 'Hello from AWS Lambda using Python\n' + get_page_title()        

def get_page_title(url="https://pythonbasics.org"):
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    return driver.title