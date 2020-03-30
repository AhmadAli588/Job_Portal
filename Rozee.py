from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.common import exceptions

driver=webdriver.Chrome(executable_path=r'C:\Users\ahmad\Desktop\chromedriver.exe')
Rozee_url="https://www.rozee.pk/"
driver.get(Rozee_url)
driver.implicitly_wait(5)
what_search=driver.find_element_by_xpath('//*[@id="search"]')
driver.implicitly_wait(5)
what_search.click()
what_search.send_keys('Accountant')
driver.implicitly_wait(5)
where_search=driver.find_element_by_xpath('//*[@id="search_form"]/div[2]/div/button')
time.sleep(10)
where_search.click()
time.sleep(5)
where_search1=driver.find_element_by_xpath('//*[@id="search_form"]/div[2]/div/div/div/input')
time.sleep(5)
where_search1.send_keys('Lahore')
# where_search1.click()
time.sleep(5)
option=driver.find_element_by_xpath('//*[@id="search_form"]/div[2]/div/div/ul')
option.click()
search_btn=driver.find_element_by_xpath('//*[@id="search_form"]/div[4]/button')
search_btn.click()
time.sleep(5)
Rozee_jobs=driver.find_elements_by_class_name('job')
# print(all_jobs)
for jobs in Rozee_jobs:
    try:
        result_html = jobs.get_attribute('innerHTML')

        #print(result_html)
    except exceptions.StaleElementReferenceException:
        pass
    soup = BeautifulSoup(result_html, 'html.parser')
    #print(soup.prettify())
    #print(soup.text)
    try:
        title = soup.find('a').text.replace('\n', '')
        # print(title)
    except:
        title = None
        # print(title)
    try:
        company = soup.findAll('a')[1].text.replace('\n', '')
        # print(company)
    except:
        company =None
        # print(company)

    try:
        company1 = soup.findAll('a')[2].text.replace('\n', '')
    except:
        company1 = None

    try:
        location = soup.findAll('a')[3].text.replace('\n', '')
        # print(company)
    except:
        location = None
    try:
        summary = soup.find('div',class_='jbody').text.replace('\n', '')
        # print(company)
    except:
        summary = None
    try:
        date = soup.find('span').text.replace('\n', '')
        # print(company)
    except:
        date = None
    try:
        salary = soup.findAll('span')[3].text.replace('\n', '')
        # print(company)
    except:
        salary = None

    print(title,company,company1,location,summary,date,salary)
    # print(title)
    sum_div = soup.find_all('div', class_='jcont')
    for a in sum_div:
        try:
            result_html1 = jobs.get_attribute('innerHTML')
            # result_html2=a.get_attribute('innerHTML')
        except exceptions.StaleElementReferenceException:
            pass
        soup1 = BeautifulSoup(result_html1, 'html.parser')
        # soup2 =  BeautifulSoup(result_html2, 'html.parser')
        try:
            cname=soup1.find('a').text.replace('\n', '')
            # print(cname)
        except:
            cname=None

        # try:
        #     # cname1=soup2.find('a') .text.replace('\n', '')
        #     # print(cname1)
        # except:
        #     cname1=None

driver.close()
