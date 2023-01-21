from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import psycopg2

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

conn = psycopg2.connect(
        database="Dash_Imo",
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
        )
        
conn.autocommit = True

cursor = conn.cursor()

caminhos = ['mxrf11', 'vghf11', 'bcff11', 'vslh11', 'game11', 'mchf11', 'hglg11', 'xpml11', 'knri11', 'hgre11', 'hgcr11', 'rztr11', 'hgru11', 'vgia11', 'vghf11', 'xpml11', 'visc11', 'mall11', 'lvbi11']


dados = []
for c in caminhos:
    navegador.get(f"https://www.fundsexplorer.com.br/funds/{c}")

    titulos_liq_dia =[]

    #Ali no final, se você botar '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[@class="carousel-cell is-selected"]//span[2]' aparecem só os números, ok
    valores_liq_dia = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[@class="carousel-cell is-selected"]//span')

    for v in valores_liq_dia: 
        v = v.text
        if v != " ":
            titulos_liq_dia.append(v)
    
    for a in titulos_liq_dia:
        a = str(a)
        a = a.replace(",",".").replace("negociações","")
        print(a)
    
'''sql = 'DROP TABLE IF EXISTS imobiliaria'
cursor.execute(sql)

sql2 = 'CREATE TABLE imobiliaria(
id SERIAL NOT NULL,
liq_dia INT NOT NULL,
ult_rend INT NOT NULL,
div_yield INT NOT NULL,
vlr_pat INT NOT NULL,
ren_mes INT NOT NULL,
p_vp INT NOT NULL,
PRIMARY KEY (id)
);'
cursor.execute(sql2)'''
