import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


 
with open('../branch_wise_list/mechanical.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    
    list_main = []
    list_fac_no = []
    list_enr_no = []
    list_MEB = []
    list_name = []
    list_odd_spi = []
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
        
        try:
            Alert(driver).text == 'Student record not found'
        
        except:
            with open ('../branch_wise_result/2nd_year_MEB_result.csv', 'a+') as output_file:
                writer = csv.writer(output_file)
                
                XPATH_FAC_NO = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[1]").text
                XPATH_ENR_NO = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[2]").text
                XPATH_NAME = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[3]").text
                XPATH_ODD_SPI = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[5]").text
                XPATH_CPI = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table[2]/tbody/tr[2]/td[6]").text
                if(XPATH_FAC_NO[fac_no_slice] == 'MEB'):
                    list_MEB.append('Mechanical')
                    
                list_odd_spi.append(XPATH_ODD_SPI)
                list_cpi.append(XPATH_CPI)
                list_fac_no.append(XPATH_FAC_NO)
                list_enr_no.append(XPATH_ENR_NO)
                list_name.append(XPATH_NAME)
            
            
                
    # dictionary for each branch
    dict_MEB = {'Faculty No': list_fac_no, 'Enrol. No': list_enr_no, 'Name': list_name, 'Branch': list_MEB, 'ODD_SPI': list_odd_spi, 'CPI': list_cpi}
    
    # making dataframe for each branch's dictionary
    df_MEB = pd.DataFrame(dict_MEB)
    
    # reseting index and appending result to csv for each branch
    df_MEB.sort_values(by='CPI', ascending=False, inplace=True)
    df_MEB.reset_index(inplace=True)
    df_MEB.drop('index', axis='columns', inplace=True)
    df_MEB.index = df_MEB.index + 1
    df_MEB.to_csv('../branch_wise_result/2nd_year_MEB_result.csv')
    
    print("Results have been extracted!")
    
    input_file.close()
    output_file.close()