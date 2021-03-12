from selenium import webdriver
from selenium.webdriver.support.ui import Select
for i in ['PAPER 1 EHG 11th Jan SHIFT 2','PAPER 1 EHG 10th Jan SHIFT 1','PAPER II EHG 8th Jan SHIFT 1','PAPER 1 EHG 11th Jan SHIFT 1','PAPER 1 EHG 10th Jan SHIFT 2','PAPER 1 EHG 9th Jan SHIFT 2','PAPER 1 EHG 9th Jan SHIFT 1','PAPER 1 EHG 12th Jan SHIFT 2','PAPER 1 EHG 12th Jan SHIFT 1','PAPER II EHG 8th Jan SHIFT 2']:
    for lp in ['JANUARY','APRIL']:
        for j in range(2,6):
            driver = webdriver.Firefox()
            driver.get('http://139.59.58.136/')
            #exam_paper = driver.find_element_by_name('e_type')
            #exam_paper.click()
            select = Select(driver.find_element_by_id('e_type'))
            select.select_by_value('JEE-MAIN')
            s2 = Select(driver.find_element_by_id('e_year'))
            s2.select_by_value('2019')
            s3 = Select(driver.find_element_by_id('e_month'))
            
            s3.select_by_value(f'{lp}')
            s4 = Select(driver.find_element_by_id('e_paper'))

            s4.select_by_value(f'{i}')
            s5 = Select(driver.find_element_by_id('e_language'))
            s5.select_by_value('ENGLISH')
            s6 = driver.find_element_by_id('mainBtn')
            s6.click()
            driver.find_element_by_id('verify').click()
            driver.find_element_by_id('mainBtn').click()
            for k in range(0,91):
                driver.find_element_by_css_selector(f'div.formField1:nth-child({j}) > input:nth-child(1)').click()
                driver.find_element_by_id('btn1').click()
            '''
            1)div.formField1:nth-child(2) > input:nth-child(1)
            2)div.formField1:nth-child(3) > input:nth-child(1)
            3)div.formField1:nth-child(4) > input:nth-child(1)
            4)div.formField1:nth-child(5) > input:nth-child(1)
            div.formField1:nth-child(2) > input:nth-child(1)
            '''
