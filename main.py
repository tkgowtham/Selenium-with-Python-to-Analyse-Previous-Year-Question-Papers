from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

def firsttime(erp=326):
    #options = Options()
    #options.headless = False options=options
    driver = webdriver.Chrome()
    driver.get('https://nta.ac.in/Quiz')

    exam_paper = driver.find_element(By.NAME, 'ExamType')
    exam_paper.click()
    select = Select(driver.find_element(By.NAME, 'ExamType'))
    select.select_by_value('1')

    #paper = driver.find_element(By.ID, 'drpExamPaper_chzn')
    #paper.click()
    select1 = Select(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div/form/div/div/div[2]/div/div/div[2]/select'))
    select1.select_by_value(f'{erp}')
    time.sleep(3)
    btn = driver.find_element(By.ID, 'btnStart')
    btn.click()
    time.sleep(3)
    
    btn_1 = driver.find_element(By.ID, 'btnLogin')
    btn_1.click()

    chk_box = driver.find_element(By.ID, '1_ch')
    chk_box.click()

    prcd = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/section/div/div/div/div/div[1]/div/a')
    prcd.click()

    submit = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[1]/div/table/tbody/tr/td[1]/div/div[2]/div/div/button')
    submit.click()
    time.sleep(3)
    
    ConfirmYes = driver.find_element(By.XPATH, '//*[@id="btnYesSubmitConfirm"]')
    ConfirmYes.click()

    ViewResult = driver.find_element(By.XPATH, '//*[@id="btnViewResult"]')
    ViewResult.click()

    no_of_q = int(driver.find_element(By.XPATH, '//*[@id="lblRTotalQuestion"]').text)
    a1 = str(driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[1]/div/div/div[1]/div/ul/li/div/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/span').text)

    print(no_of_q)

    listofans = []
    for no in range(1, (no_of_q // 10) + 1):
        for io in range(1, 11):
            if io % 2 == 0:
                oe = 'even'
            else:
                oe = 'odd'
            try:
                kk = int(driver.find_element(By.CSS_SELECTOR, f'tr.{oe}:nth-child({io}) > td:nth-child(4)').text)
                listofans.append(kk)
            except ValueError:
                print('No Value')
                listofans.append('0')
                continue
            '''if io % 10 == 0:
                ci = driver.find_element(By.XPATH, '//*[@id="divPaging"]/ul/li[10]/a')
                ci.click()'''

    driver.quit()

    print(listofans)

    dic1 = {'1': 0, '2': 0, '3': 0, '4': 0}
    for i in listofans:
        if i == 1:
            dic1['1'] += 1
        elif i == 2:
            dic1['2'] += 1
        elif i == 3:
            dic1['3'] += 1
        elif i == 4:
            dic1['4'] += 1

    print(dic1)

    for i in range(1, 5):
        a2 = no_of_q
        a3 = no_of_q
        a4 = dic1[f'{i}']
        a5 = 90 - dic1[f'{i}']
        a7 = a4 * 4
        a8 = a5 * (-1)
        a6 = a7 + a8

        a = 'Exam Name:' + str(a1)
        b = 'Total Question:' + str(a2)
        c = 'Attempted Question:' + str(a3)
        d = 'Correct Answers:' + str(a4)
        e = 'Incorrect Answers:' + str(a5)
        f = 'Score:' + str(a6)
        h = 'Correct Score: ' + str(a7)
        j = 'Incorrect Score: ' + str(a8)

        s = (a + ' , ' + f'Choosen Option: {i}' + ' , ' + b + ' , ' + c + ' , ' + d + ' , ' + e + ' , ' + f + ' , ' + h + ' , ' + j)

        with open('exammark.txt', 'a') as g:
            g.write(f'{s}\n')
            if i == 4:
                g.write('\n')


#for i in [311, 310, 308, 299, 161, 155, 153, 151, 150, 148, 146, 145, 144, 143, 140, 138, 133, 1]:
#    firsttime(i)
firsttime()
