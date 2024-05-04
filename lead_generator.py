from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv

search_query = "breweries Austin Texas"
wait = WebDriverWait(driver, 5)

driver = webdriver.Chrome("path-to-chrome-driver")
driver.get("https://www.google.com/maps")

links_list = []
names_list = []
business_types_list = []
ratings_list = []
num_reviews_list = []
addresses_list = []
websites_list = []
numbers_list = []

# Locate search input and enter query
search_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='searchboxinput']")))
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Locate side bar and scroll to end of results
divSideBar = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')))

keepScrolling = True
while keepScrolling:
    divSideBar.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    divSideBar.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    html = driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
    if(html.find("You've reached the end of the list.") != -1):
        keepScrolling = False

# Append links and business names
links = driver.find_elements(By.CLASS_NAME, 'hfpxzc')

for link in links:
	links_list.append(link.get_attribute('href'))
	names_list.append(link.get_attribute('aria-label'))

# Append Phone Number
numbers = driver.find_elements(By.CLASS_NAME, 'UsdlK')

for number in numbers:
	numbers_list.append(number.text)

page_count = 0

print(f'Pages found: {len(links_list)}\n')

# Go to each link
for i in range(len(links_list)):
	driver.get(links_list[i])

	# Append Business Type
	business_type = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='DkEaL ']")))
	business_types_list.append(business_type.text)

	# Append Business Rating
	business_rating = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ceNzKf")))
	ratings_list.append(business_rating.get_attribute('aria-label').split(' stars')[0])

	# Append Number of Reviews
	num_of_reviews = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span")))
	num_reviews_list.append(num_of_reviews.text[1:-1])

	# Scroll down
	divSideBar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#QA0Szd > div > div > div.w6VYqd > div.bJzME.tTVLSc > div > div.e07Vkf.kA9KIf')))
	divSideBar.send_keys(Keys.PAGE_DOWN)
	time.sleep(1.5)
	divSideBar.send_keys(Keys.PAGE_DOWN)
	time.sleep(1.5)

	# Append Address
	address = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Io6YTe fontBodyMedium kR99db ']")))
	addresses_list.append(address.text)

	# Append Website
	website = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='rogA2c ITvuef']")))
	websites_list.append(website.text)

	page_count += 1
	print(f'Pages Extracted: {page_count}')

driver.quit()

print('\nData Extraction Complete\n')
print('Exporting to CSV...')

with open('gmaps_leads.csv', 'w') as f:
	writer = csv.writer(f)
	try:
		writer.writerow(['Name', 'Type', 'Rating', 'Num of Reviews', 'Addresses', 'Websites', 'Phone Numbers'])

		for i in range(len(links_list)):
			writer.writerow([names_list[i], business_types_list[i], ratings_list[i], num_reviews_list[i], addresses_list[i], websites_list[i], numbers_list[i]])

	except:
		writer.writerow(['Error', 'Error', 'Error', 'Error', 'Error', 'Error', 'Error'])

print('Process Complete')
