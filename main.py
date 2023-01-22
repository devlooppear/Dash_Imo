from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import psycopg2

def Browser_Concet():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    return navegador

def Init_Psycopg():

    conn = psycopg2.connect(
            database="Dash_Imo",
            user='postgres',
            password='postgres',
            host='localhost',
            port='5432'
            )
            
    conn.autocommit = True

    cursor = conn.cursor()
    return cursor

def Criar_Tabela(cursor):
    sql = 'DROP TABLE IF EXISTS imobiliaria'
    cursor.execute(sql)

    sql = f'''CREATE TABLE imobiliaria(
    id SERIAL NOT NULL,
    nomes_cam VARCHAR (10) NOT NULL,
    liq_dia INT NOT NULL,
    ult_rend FLOAT NOT NULL,
    div_yield FLOAT NOT NULL,
    pat_liq FLOAT NOT NULL,
    vlr_pat FLOAT NOT NULL,
    ren_mes FLOAT NOT NULL,
    p_vp FLOAT NOT NULL,
    PRIMARY KEY (id)
    );'''
    cursor.execute(sql)

def Achar_Tratar_Inserir(navegador,cursor):
    caminhos = ['mxrf11', 'vghf11', 'bcff11', 'vslh11', 'game11', 'mchf11', 'hglg11', 'xpml11', 'knri11', 'hgre11', 'hgcr11', 'rztr11', 'hgru11', 'vgia11', 'vghf11', 'xpml11', 'visc11', 'mall11', 'lvbi11']

    for caminho in caminhos:

        navegador.get(f"https://www.fundsexplorer.com.br/funds/{caminho}")

        titulos_cam = []

        titulos_cam.append(caminho)

        titulos_liq_dia =[]

        valores_liq_dia = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[1][@class="carousel-cell is-selected"]//span[2]')

        for vlr_liq in valores_liq_dia: 
            vlr_liq = vlr_liq.text
            if vlr_liq != " ":
                titulos_liq_dia.append(vlr_liq)
            print(vlr_liq)

        titulos_ult_rend =[]

        valores_ult_rend = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[2][@class="carousel-cell is-selected"]//span[2]')

        for vlr_ult in valores_ult_rend: 
            vlr_ult = vlr_ult.text
            if vlr_ult != " ":
                titulos_ult_rend.append(vlr_ult)
        
        titulos_div_yield =[]

        valores_div_yield = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[3][@class="carousel-cell is-selected"]//span[2]')

        for vlr_div in valores_div_yield: 
            vlr_div = vlr_div.text
            if vlr_div != " ":
                titulos_div_yield.append(vlr_div)

        titulos_pat_liq =[]

        valores_pat_liq = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[4][@class="carousel-cell is-selected"]//span[2]')

        for vlr_pat_liq in valores_pat_liq: 
            vlr_pat_liq = vlr_pat_liq.text
            if vlr_pat_liq != " ":
                titulos_pat_liq.append(vlr_pat_liq)

        titulos_pat =[]

        valores_pat = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[5][@class="carousel-cell is-selected"]//span[2]')

        for vlr_pat in valores_pat: 
            vlr_pat = vlr_pat.text
            if vlr_pat != " ":
                titulos_pat.append(vlr_pat)
        
        titulos_ren_mes =[]

        valores_ren_mes = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[6][@class="carousel-cell is-selected"]//span[2]')

        for vlr_ren in valores_ren_mes: 
            vlr_ren = vlr_ren.text
            if vlr_ren != " ":
                titulos_ren_mes.append(vlr_ren)
        
        titulos_p_vp = []

        valores_p_vp = navegador.find_elements(By.XPATH, '//div[@id="main-indicators-carousel"]//div[@class="flickity-viewport"]//div[@class="flickity-slider"]//div[7][@class="carousel-cell is-selected"]//span[2]')

        for vlr_p in valores_p_vp: 
            vlr_p = vlr_p.text
            if vlr_p != " ":
                titulos_p_vp.append(vlr_p)
    
        for cam,a,b,c,d,e,f,d in list(zip(titulos_cam,titulos_liq_dia,titulos_ult_rend,titulos_div_yield,titulos_pat_liq,titulos_pat,titulos_ren_mes,titulos_p_vp)):

            for a in titulos_liq_dia:
                a = str(a)
                a = a.replace(".","")
                print(a)
            
            for b in titulos_ult_rend:
                b = str(b)
                b = b.replace(",",".").replace("R","").replace("$","").replace(" ","")
                print(b)

            for c in titulos_div_yield:
                c = str(c)
                c = c.replace(",",".").replace("%","")
                print(c)

                
            for d in titulos_pat_liq:
                d = str(d)
                if "mi" in d:
                    d = d.replace(",",".").replace("R","").replace("$","").replace(" ","").replace("mi","").replace(".","").replace("bi","")
                    nv_tmn = 9-len(d)
                    d = d.replace(d,d + '0'*nv_tmn)
                elif "bi" in d:
                    d = d.replace(",",".").replace("R","").replace("$","").replace(" ","").replace("mi","").replace(".","").replace("bi","")
                    nv_tmn = 12-len(d)
                    d = d.replace(d,d + '0'*nv_tmn)
                else:
                    d = d.replace(",",".").replace("R","").replace("$","").replace(" ","").replace("mi","").replace(".","").replace("bi","")
                print(d)

            for e in titulos_pat:
                e = str(e)
                e = e.replace(",",".").replace("R","").replace("$","").replace(" ","")
                print(e)

            for f in titulos_ren_mes:
                f = str(f)
                f = f.replace(",",".").replace("%","")
                print(f)
            for g in titulos_p_vp:
                g = str(g)
                g = g.replace(",",".")
                print(g)

            sql = f'''INSERT INTO imobiliaria (nomes_cam,liq_dia,ult_rend,div_yield,pat_liq,vlr_pat,ren_mes,p_vp) VALUES ('{cam}','{int(a)}','{float(b)}','{float(c)}','{int(d)}','{float(e)}','{float(f)}','{float(g)}')'''
            cursor.execute(sql)

def main():

    navegador = Browser_Concet()
    cursor, navegador = Init_Psycopg()
    Criar_Tabela(cursor)
    Achar_Tratar_Inserir(navegador,cursor)

main()