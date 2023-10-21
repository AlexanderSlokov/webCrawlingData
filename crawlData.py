from datetime import datetime, timedelta
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# import browser Chrome for Selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

current_date = datetime(2023,10,4)
data=[]

# Read utl
idx = 0

while True:
   # print("Process 300 days from {}-{}-{}".format(current_date.day, current_date.month, current_date.year))
    url = 'https://www.thantai1.net/so-ket-qua'
    browser.get(url)

    # Set date for "date" textbox, this textbox on the web has a id value = "end"
    end = browser.find_element(by="id", value="end")
    end.clear()
    end.send_keys("{}-{}-{}".format(current_date.day, current_date.month, current_date.year))

    # How much result will be output
    # point to the "300" day button by Xpath
    btn = browser.find_element(By.XPATH, '/html/body/div[3]/main/div/form/div[2]/div/button[9]')
    btn.click()

    # Get results, remember to change spacing to dots "."
    results = browser.find_elements(By.CLASS_NAME,'font-weight-bold.text-danger.col-12.d-block.p-1.m-0')
    for row in results:
        print(row.text)
        idx += 1
        data.append(row.text)

    current_date -= timedelta(days=300)
    # sleep(1)
    if idx > 20 * 365:
        break

df = pd.DataFrame(data, columns=['Ket Qua'])
df.to_csv("XSMB.csv", index=False)
browser.close()
