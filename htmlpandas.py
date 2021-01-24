# from selenium import webdriver
# import pandas as pd
# import requests
# import csv
# from bs4 import BeautifulSoup as bs

# # url = "https://www.w3schools.com/html/html_tables.asp"
# url = "http://titania.saeima.lv/LIVS13/SaeimaLIVS2_DK.nsf/0/52A297A4B98224ECC22584B9007E5875?OpenDocument"
# text = requests.get(url).text
# html = bs(text, "html.parser")
# div = html.find('div', id='mainContentHolder')
# # div = html
# print div

# table = div.find_all('table')
# print table

# # table = html.find('table', id='customers')

# data = [[td.text for td in tr.find_all('td')] for tr in table.find_all('tr')]
# f = open('output.csv', 'w')
# w = csv.writer(f)
# for row in data:
#     w.writerow(row)
# f.close()


# # URL = "https://en.wikipedia.org/wiki/Cricket_World_Cup"
# url = "http://titania.saeima.lv/LIVS13/SaeimaLIVS2_DK.nsf/0/52A297A4B98224ECC22584B9007E5875?OpenDocument"
# # tables = pd.read_html(URL)
# # page = requests.get(URL)
# # text = requests.get(URL).text
# # div = text.find('script')

# # print text


# driver = webdriver.PhantomJS()
# driver.get(url)
# mainContentHolder = driver.find_element_by_id(id_='mainContentHolder')
# table_string = mainContentHolder.text
# table_html = mainContentHolder.get_attribute('innerHTML')
# # print(table_html)

# panda_html = pd.read_html(table_html)

# panda_table = panda_html[0]

# print(panda_table)
# # df = pd.DataFrame(panda_html)
# # print(df)
# panda_table.to_csv('panda.csv')


# # f = open('output.csv', 'w')
# # w = csv.writer(f)

# # for row in panda_html:
# #     print(row)
# #     w.writerow(row)
# # f.close()

# # print(table_string)

# # reader = csv.reader(table_string.split('\n'))
# # reader = '\t'.join(reader1).split('   ')

# # newList = []
# # for row in reader:
# #     print(row)

# # for row in reader:
# #     # print(row.split('   '))
# #     formatted_row = '\t'.join(row).split('   ')
# #     for item in formatted_row:
# #         # print(item)
# #         newList.append(item)
# #         pass
# #     # print(formatted_row.type)
# #     # w.writerow(row)

# #     # for string in formatted_row
# #     # print(string)
# #     # w.writerow(string)
# # print(newList)

# # for row in newList:
# #     print(row)
# #     w.writerow(row)

# # f.close()

# # f = open('output.csv', 'w')
# # w = csv.writer(f)
# # for row in mainContentHolder:
# #     w.writerow(row)
# # f.close()

# # html_content = requests.get(url).text
# # soup = bs(html_content, "lxml")

# # #print(soup.findAll("div", {"class": "mainInfoTable"}))

# # gdp_table = soup.find("table", attrs={"class": "mainVoteTable"})
# # # print(gdp_table)

# # gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

# # # Get all the headings of Lists
# # headings = []
# # for td in gdp_table_data[0].find_all("td"):
# #     # remove any newlines and extra spaces from left and right
# #     headings.append(td.b.text.replace('\n', ' ').strip())

# # print(headings)

# # # url = "https://www.w3schools.com/html/html_tables.asp"
# # url = "http://titania.saeima.lv/LIVS13/SaeimaLIVS2_DK.nsf/0/52A297A4B98224ECC22584B9007E5875?OpenDocument"
# # text = requests.get(url).text
# # html = bs(text, "html.parser")
# # div = html.find('div', id='mainContentHolder')
# # # div = html
# # print div

# # table = div.find_all('table')
# # print table

# # # table = html.find('table', id='customers')

# # data = [[td.text for td in tr.find_all('td')] for tr in table.find_all('tr')]
# # f = open('output.csv', 'w')
# # w = csv.writer(f)
# # for row in data:
# #     w.writerow(row)
# # f.close()
