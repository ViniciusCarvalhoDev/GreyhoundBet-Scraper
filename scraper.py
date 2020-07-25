import requests 
import selenium
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
from lxml import builder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from termcolor import colored
import logging

#caminho para o webDriver, modificar de acordo com o seu computador
PATH = "C:\\Users\\GABRIELA\\Documents\\python_testes\\chromedriver.exe"
#url da pagína que se pretende extrair os dados
url = "https://greyhoundbet.racingpost.com/#dog/race_id=1776769&r_date=2020-07-25&dog_id=529993"

#----------------------------------------------

def collect_table (lista):

    try:
        balao = WebDriverWait(driver,10).until(
        Ec.presence_of_element_located((By.ID,"sortableTable"))
        
    )
    finally:
        logging.info("Starting to collect")

    text = driver.page_source
    soup = BeautifulSoup(text,"lxml")

    tabela = soup.find("table", attrs={"class":"formGrid"})
    tabela_conteudo = tabela.find('tbody')
    rows = tabela_conteudo.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        print (colored('Collecting Data...','red'))
        cols = [ele.text.strip() for ele in cols]
        lista.append([ele for ele in cols if ele])
    
    page_down = driver.find_element_by_id('pager-down')
    page_down.click()
    time.sleep(3)


if __name__ == "__main__":

    driver = webdriver.Chrome(PATH)
    driver.get(url)

    landing_btn = driver.find_element_by_id('landingBookiesList')
    landing_btn.click()

    driver.execute_script('document.getElementById("landingWHStart").click()')

    data = []

    for x in range(5):
        collect_table(data)

    print(data)
    print("                  ")
    print("PROCESSO COMPLETO!")

    f= open("dados_tabela.txt","w+")
    f.write(str(data))
    f.close()
    driver.quit()

    print("                  ")
    print("DADOS ARMAZENADOS")
