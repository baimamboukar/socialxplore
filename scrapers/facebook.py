from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# declare driver as global variable
global driver
options = Options()

# add arguments to the web driver options
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
driver = webdriver.Chrome(executable_path="./helpers/chromedriver",
                          options=options)
driver.get("https://en-gb.facebook.com")
driver.maximize_window()