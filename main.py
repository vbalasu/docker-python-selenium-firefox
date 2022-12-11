# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return get_page_title()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


def get_page_title(url="https://pythonbasics.org"):
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    return driver.title