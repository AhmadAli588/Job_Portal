from django.shortcuts import render,redirect
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.common import exceptions
from .models import Scrape

# def home(request):
#     if request.method == 'POST':
#         driver = webdriver.Chrome(executable_path=r'C:\Users\ahmad\Desktop\chromedriver.exe')
#         url = "https://www.indeed.com.pk/jobs?q=django Developer&l=Lahore&start="
#         scrape_m=Scrape()
#         for i in range(0, 5, 1):
#             driver.get(url + str(i))
#             driver.implicitly_wait(0)
#             all_jobs =driver.find_elements_by_class_name('result')
#             for jobs in all_jobs:
#                 result_html = jobs.get_attribute('innerHTML')
#                 soup = BeautifulSoup(result_html, 'html.parser')
#
#                 try:
#                     scrape_m.title = soup.find('a', class_="jobtitle").text.replace('\n', '')
#                 except:
#                     scrape_m.title = None
#                 try:
#                     scrape_m.location = soup.find(class_="location").text
#                 except:
#                     scrape_m.location = None
#                 try:
#                     scrape_m.company = soup.find(class_="company").text.replace('\n', '').strip()
#                 except:
#                     scrape_m.company = None
#                 try:
#                     scrape_m.salary = soup.find(class_="salary").text.replace('\n', '').strip()
#                 except:
#                     scrape_m.salary = None
#                 try:
#                     scrape_m.sponsored = soup.find(class_="sponserdGray").text
#                     scrape_m.sponsored = "Sponsored"
#                 except:
#                     scrape_m.sponsored = "Organic"
#
#                 sum_div = soup.find_all('div', class_='summary')
#                 for ul in sum_div:
#                     result_html1 = jobs.get_attribute('innerHTML')
#                     soup1 = BeautifulSoup(result_html1, 'html.parser')
#
#                     scrape_m.description = soup1.find('ul').text.replace('\n', '')
#                 try:
#                     close_btn =driver.find_element_by_class_name("popover-x-button-close")
#                     close_btn.click()
#                 except:
#                     pass
#                 scrape_m.save()
#             scrape_o=Scrape.objects.all()
#         return render(request, 'Home/Scrape.html',{"scrape_o":scrape_o} )
#
#     else:
#          return render(request, 'Home/home.html')
def home(request):
    if request.method=='POST':
        driver = webdriver.Chrome(executable_path=r'C:\Users\ahmad\Desktop\chromedriver.exe')
        url = "https://www.indeed.com.pk/jobs?"
        what=request.POST['what']
        where=request.POST['where']
        try:
            driver.get(url)
            driver.implicitly_wait(3)
            serach_what = driver.find_element_by_xpath('//*[@id="text-input-what"]')
            serach_what.send_keys(what)
            serach_where = driver.find_element_by_xpath('//*[@id="text-input-where"]')
            serach_where.send_keys(where)
            driver.implicitly_wait(3)
            serach_button = driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
            serach_button.click()
            base_url=driver.current_url
            page="&start="

        except:
            pass
        all_data = []
        for i in range(0, 5, 1):
            driver.get(base_url+page + str(i))
            driver.implicitly_wait(0)
            all_jobs =driver.find_elements_by_class_name('result')
            for jobs in all_jobs:
                try:
                    result_html = jobs.get_attribute('innerHTML')
                except exceptions.StaleElementReferenceException:
                    pass

                soup = BeautifulSoup(result_html, 'html.parser')
                try:
                    close_btn = driver.find_element_by_class_name("popover-x-button-close")
                    close_btn.click()
                except:
                    pass
                try:
                    title = soup.find('a', class_="jobtitle").text.replace('\n', '')
                except:
                    title = None
                try:
                    location = soup.find(class_="location").text
                except:
                    location = None
                try:
                    company = soup.find(class_="company").text.replace('\n', '').strip()
                except:
                    company = None
                try:
                    salary = soup.find(class_="salary").text.replace('\n', '').strip()
                except:
                    salary = None
                try:
                    date = soup.find(class_="date").text

                except:
                    date = None

                sum_div = soup.find_all('div', class_='summary')
                for ul in sum_div:
                    try:
                        result_html1 = jobs.get_attribute('innerHTML')
                    except exceptions.StaleElementReferenceException:
                        pass
                    soup1 = BeautifulSoup(result_html1, 'html.parser')

                    description = soup1.find('ul').text.replace('\n', '')
                try:
                    close_btn =driver.find_element_by_class_name("popover-x-button-close")
                    close_btn.click()
                except:
                    pass
                all_data.append({
                    "title": title,
                    "Location": location,
                    "Company": company,
                    "Salary": salary,
                    "Date": date,
                    "Description": description
                })

        driver.close()
        return render(request,'Home/Scrape.html',{"Scrapes":all_data})

    else:
        return render(request, 'Home/home.html')

                #print(title, location, company, salary, sponsored, description)
                # data_frame = pd.DataFrame(
                #     columns=["Title", "Location", "Company", "Salary", "Sponsored", "Description"])
                #
                # data_frame = data_frame.append(
                #     {'Title': title, 'Location': location, 'Company': company, 'Salary': salary,
                #      'Sponsored': sponsored, 'Description': description}, ignore_index=True)


