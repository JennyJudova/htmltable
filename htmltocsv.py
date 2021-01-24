import pandas as pd
from selenium import webdriver

url = "http://url"

driver = webdriver.PhantomJS()

driver.get(url)

mainContentHolder = driver.find_element_by_id(id_='mainContentHolder')
table_string = mainContentHolder.text
table_html = mainContentHolder.get_attribute('innerHTML')
panda_html = pd.read_html(table_html)
panda_table = panda_html[0]
data1 = panda_table.iloc[1:, ]

d1 = data1.drop(panda_table.columns[[4, 5, 6, 7, 8]], axis=1)
d2 = data1.drop(panda_table.columns[[0, 1, 2, 3, 4]], axis=1)
d1.columns = ['id', 'Vārds', 'Frakcija', 'Balss']
d2.columns = ['id', 'Vārds', 'Frakcija', 'Balss']

data3 = pd.concat([d1, d2], ignore_index=True, sort=False)
d3 = data3.iloc[1:, ]
d3.to_csv('panda3.csv', index=False, index_label=False)

# Add a case for a row with no ID - they have to be deleted.
