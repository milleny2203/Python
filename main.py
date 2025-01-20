from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

## importar o driver do chrome
driver_path = "/usr/local/bin/chromedriver"  
service = Service(driver_path)

## chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  
#options.add_argument("--headless")  # Executar sem interface gráfica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--enable-logging")
options.add_argument("--v=1")
options.add_experimental_option("detach",True) # manter navegador aberto


driver = webdriver.Chrome(service=service, options=options)
driver.get("https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M&utm_campaign=programacao&utm_content=python%2Fminicurso%2Fminicurso-automacao%2Finscricao&conversion=lespy-jan-25")

## Pegar elemento e escrever
time.sleep(3)
driver.find_element('xpath'
, '//*[@id="firstname"]').send_keys('milleny')

driver.find_element('xpath'
, '//*[@id="email"]').send_keys('millenynoalsantos@gmail.com')

driver.find_element('xpath'
, '//*[@id="phone"]').send_keys('17996657544')


## Pegar elemento e clicar no botao
driver.find_element('xpath', '//*[@id="_form_1925_submit"]').click()
time.sleep(5)
driver.find_element('xpath', '//*[@id="botao-minicurso"]').click()









