# Import Necessary Libraries From Selenium, Pandas, and Time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

ex_path = "C:/Users/joshu/Desktop/web scraping/yelp scrape/yelp_thai_data.csv"
og_site = "https://www.yelp.com/search?find_desc=Best+Thai+Food&find_loc=Santa+Ana%2C+CA"
max_pop = 3


# Initialize Driver
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
# options.add_argument('--single-process')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--incognito')
options.add_argument('--disable-blink-features=AutomationControlled')

options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("disable-infobars")
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def get_prices(cur_driver):
    # Gets all the prices of the full menu and min max and average
    cost_paths = cur_driver.find_elements("xpath", "//li[contains(@class, 'menu-item-price-amount')]")
    all_prices = []
    for cur_cost in cost_paths:
        all_prices.append(float(cur_cost.get_attribute("innerHTML").strip().replace("$", "")))
    return min(all_prices), max(all_prices), round(sum(all_prices)/len(all_prices), 2)


def get_contact(cur_driver):
    # gets the website, phone number, and address info and top dishes
    try:
        web_path = cur_driver.find_element("xpath", "//div[.//p[text()[contains(., 'Business website')]]][count(.//div)=0]//a")
        cur_web = web_path.get_attribute("innerHTML")
    except:
        cur_web = None
        print("Unable to Collect Website :C")

    try:
        num_path = cur_driver.find_element("xpath", "//div[.//p[text()[contains(., 'Phone number')]]][count(.//div)=0]//p[text()[not(contains(., 'Phone number'))]]")
        cur_num = num_path.get_attribute("innerHTML")
    except:
        cur_num = None
        print("Unable to Collect Phone Number :C")

    try:
        add_path = cur_driver.find_elements("xpath", "//address//span")
        cur_add = ""
        for add_part in add_path:
            cur_add += add_part.get_attribute("innerHTML")
    except: 
        cur_add = None
        print("Unable to Collect Address :C")

    try:
        review_path = cur_driver.find_element("xpath", "//div[contains(@class, 'rating-text')]//p")
        cur_review = review_path.get_attribute("innerHTML")
    except:
        cur_review = None
        print("Unable to Total Reviews :C")

    try:
        pop_paths = cur_driver.find_elements("xpath", "//div[.//span[text()[contains(., 'Photos')]]][count(.//div)=1]//p")
        pop_paths = pop_paths
        cur_pop = list(map(lambda x: x.get_attribute("innerHTML"), pop_paths))
    except:
        cur_pop = None
        print("Unable to Popular Items :C")
    
    return cur_web, cur_num, cur_add, cur_review, cur_pop
    

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options = options)
driver.get(og_site)
time.sleep(1.5)

# all paths and restaurant names
rest_path = driver.find_elements("xpath", "//ul//div[count(.//img)=0]//span[count(.//*)=1 and count(.//a)=1]//a[text()[not(contains(., 'more'))]]")

rest_df = pd.DataFrame()

for cur_path in rest_path:
    driver2 = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                              options = options)
    cur_name = cur_path.get_attribute("innerHTML")
    cur_yelp = cur_path.get_attribute("href")
    print()
    print("Loading Website Company: " + cur_name)
    driver2.get(cur_yelp)
    time.sleep(1.5)
    cur_web, cur_num, cur_add, cur_review, cur_pop = get_contact(driver2)
    print("Contact Info Collected!")

    try:
        menu_path = driver2.find_element("xpath", "//div[.//span[text()[contains(., 'Full menu')]]][count(.//div)=3]//a")
        driver2.get(menu_path.get_attribute("href"))
        time.sleep(1.5)
        cur_min, cur_max, cur_average = get_prices(driver2)
        print("Prices Collected!")
    except:
        cur_min = None
        cur_max = None
        cur_average = None
        print("Unable to Collect Prices :C")
    
    
    temp_df = pd.DataFrame({"Name": [cur_name],
                            "Yelp": [cur_yelp],
                            "Website": [cur_web],
                            "Phone": [cur_num],
                            "Address": [cur_add],
                            "Review": [cur_review],
                            "Average Price": [cur_average],
                            "Minimum Price": [cur_min],
                            "Maximum Price": [cur_max]})
    for pop_i in range(max_pop):
        if pop_i >= len(cur_pop):
            temp_df["Popular_Dish" + str(pop_i+1)] = None
        else:
            temp_df["Popular_Dish" + str(pop_i+1)] = cur_pop[pop_i]
    rest_df = pd.concat([rest_df, temp_df]).reset_index(drop = True)
    rest_df.to_csv(ex_path, index = False)
    driver2.close()
driver.close()
print(rest_df)