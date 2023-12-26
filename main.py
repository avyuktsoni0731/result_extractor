import csv
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


 
with open('old_data.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    
    list_main = []
    list_fac_no = []
    list_enr_no = []
    list_name = []
    list_branch = []
    list_odd_spi = []
    list_even_spi = []
    list_cpi = []
    
    fac_no_slice = slice(2, 5, 1)
    
    for i in reader:
        list_main.append(i)
    for j in list_main:
        driver = webdriver.Chrome()
        driver.get(url="https://ctengg.amu.ac.in/web/st_result001.php?prog=btech")
        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[1]/td/input").send_keys(j[0])
        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[2]/td/input").send_keys(j[1])
        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/table/tbody/tr[5]/td/button").click()
        
        with open ('results_old.csv', 'a+') as output_file:
            writer = csv.writer(output_file)
            XPATH_FAC_NO = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[1]").text
            XPATH_ENR_NO = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[2]").text
            XPATH_NAME = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[3]").text
            XPATH_EVEN_SPI = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[5]").text
            XPATH_CPI = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[6]").text
            
            
            list_fac_no.append(XPATH_FAC_NO)
            list_enr_no.append(XPATH_ENR_NO)
            list_name.append(XPATH_NAME)
            if(XPATH_FAC_NO[fac_no_slice] == 'COB'):
                list_branch.append('Computer')
            elif(XPATH_FAC_NO[fac_no_slice] == 'AIB'):
                list_branch.append('Artificial Intelligence')
            elif(XPATH_FAC_NO[fac_no_slice] == 'ELB'):
                list_branch.append('Electronics')
            elif(XPATH_FAC_NO[fac_no_slice] == 'EEB'):
                list_branch.append('Electrical')
            elif(XPATH_FAC_NO[fac_no_slice] == 'MEB'):
                list_branch.append('Mechanical')
            elif(XPATH_FAC_NO[fac_no_slice] == 'CEB'):
                list_branch.append('Civil')
            elif(XPATH_FAC_NO[fac_no_slice] == 'CHB'):
                list_branch.append('Chemical')
            elif(XPATH_FAC_NO[fac_no_slice] == 'AEB'):
                list_branch.append('Automobile')
            elif(XPATH_FAC_NO[fac_no_slice] == 'FTB'):
                list_branch.append('Food Technology')
            else:
                list_branch.append('Petrochemical')
            list_even_spi.append(XPATH_EVEN_SPI)
            list_cpi.append(XPATH_CPI)
                
    dict = {'Faculty No': list_fac_no, 'Enrol. No': list_enr_no, 'Name': list_name, 'Branch': list_branch, 'Even_SPI': list_even_spi, 'CPI': list_cpi}
    df = pd.DataFrame(dict)
    dr = df.reset_index()
    df.index = df.index + 1
    df.to_csv('results_old.csv')
    
    input_file.close()
    output_file.close()