import requests as requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import xlsxwriter

"""options"""
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0")

#headless mode
options.headless = True
options.add_argument('--disable-dev-shm-usage')

#disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome("./chromedriver", options=options)

expenses = ([])


def data_samples(url):
    driver.get(url)
    for link in range(1, 5):
        driver.find_elements_by_class_name("block-link__overlay-link")[link].click()
        time.sleep(4)
        links = driver.current_url
        req = requests.get(links)
        soup = BeautifulSoup(req.text, 'lxml')
        title = soup.find('h1', class_="ssrcss-15xko80-StyledHeading e1fj1fc10").text
        text = soup.find('p', class_="ssrcss-1q0x1qg-Paragraph eq5iqo00").text
        print(links)
        expenses.append([links, title, text],)
        save_data()
        driver.back()
        continue


def save_data():
    workbook = xlsxwriter.Workbook('Expenses02.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    for item, cost, t in (expenses):
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost)
        worksheet.write(row, col + 2, t)

        row += 1

    workbook.close()


data_samples('https://www.bbc.com/')

