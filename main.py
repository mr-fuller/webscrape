from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
# from credentials
with open("credentials.json") as creds:
    credentials = json.load(creds)

browser = webdriver.Firefox("C:/geckodriver24_win32")
browser.get("https://gis.dot.state.oh.us/tims/Data/Download")
# accordianElem = browser.find_element_by_class_name("container-fluid")
# accordianElem.send_keys(Keys.TAB)
# accordianElem.send_keys(Keys.TAB)
# accordianElem.send_keys(Keys.TAB)
# accordianElem.send_keys(Keys.ENTER)


#click the link to the data download page

#find email element
# emailElem = browser.find_element_by_id()
# emailElem.send_keys(credentials['tims_id'])

#find password element
# passwordElem = browser.find_element_by_id()
# passwordElem.send_keys(credentials['tims_password'])
# LoginElem = browser.find_element_by_xpath(/html/body/footer/div/div/div[2]/ul/li[8]/form/input[2]).click()
# LoginElem.send_keys()
# browser.find_elements_by_class_name()
# This opens the Roadway Information Section
browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[4]/div/div[3]/div[1]/a").send_keys(Keys.ENTER)
# This selects the Road Inventory file
browser.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[4]/div/div[3]/div[2]/div/div[15]/button").send_keys(Keys.ENTER)

# for panel in :
#     # print(item)
#     if panel.text == "Roadway Information":
#         panel.click()
# for item in browser.find_elements_by_class_name("btn btn-block btn-default layer-item"):
#     if item.text == "Road Inventory":
#         item.click()


# browser.find_element_by_link_text("Road Inventory").click()

browser.find_element_by_id('export-btn').click()
browser.find_element_by_id('export-kml').click()