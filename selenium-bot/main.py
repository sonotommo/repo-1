# pip install selenium
# pip install webdriver-manager

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

SPOTIFY_URL = 'https://open.spotify.com/search'

username = 'username'
password = 'password'

# software installato nel pc
chrome_driver = ChromeDriverManager().install()
# driver serve per assegnare ordini al nostro browser
driver = Chrome(service=Service(chrome_driver))
# mettere a schermo intero chrome
driver.maximize_window()

# aprire pagina
driver.get(SPOTIFY_URL)

driver.find_element(By.CLASS_NAME, 'kuwYvr').click()
sleep(1)

# trovare input username e password
username_input = driver.find_element(By.ID, 'login-username')
password_input = driver.find_element(By.ID, 'login-password')

# inserire username e password
username_input.send_keys(username)
password_input.send_keys(password)

# trovare bottone di invio dei dati
button = driver.find_element(By.CLASS_NAME, 'ButtonInner-sc-14ud5tc-0')
button.click()

sleep(2)
# trovare form input
form = driver.find_element(By.CLASS_NAME, 'hGXzYa')
form.send_keys('acdc')


# l'input serve per mantenere il browser aperto
input()