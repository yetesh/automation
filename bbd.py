from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import names
import mailslurp_client

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = "api-key"

inbox = None

with mailslurp_client.ApiClient(configuration) as api_client:
	api_instance = mailslurp_client.InboxControllerApi(api_client)
	inbox = api_instance.create_inbox()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--log-level=3')

# Provide the path of chromedriver present on your system
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",
                          chrome_options=options)
driver.set_window_size(1920,1080)

# Send a get request to the url
driver.get('https://blackbeardiner.fbmta.com/members/UpdateProfile.aspx')

name = names.get_full_name().split(" ")

driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_FirstName_0").send_keys(name[0])
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_LastName_0").send_keys(name[1])
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_EmailAddress_0").send_keys(inbox.email_address)
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_EmailAddress_1").send_keys(inbox.email_address)
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_Birthdate_0").send_keys("December")
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_Birthdate_0_Day").send_keys("10")
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_Birthdate_0_Year").send_keys("1990")
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_Zip_0").send_keys("94105")
driver.find_element(By.ID, "ctl00_PageContent_MemberProfileControl_CustomField_StoreCode_0").send_keys("CA - Colma (4927 Junipero Serra Blvd.)")

driver.find_element(By.ID, "ctl00_PageContent_SubmitImage").send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()