
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC

loginCredentials = { 
    "username": "m.mohamed2400718", 
    "password": "Hello.py503"
}

data = {}
driver = webdriver.Chrome()
driver.get("https://lms.badyauni.edu.eg/my/courses.php")

errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)

if(driver.title == "Log in to the site | Badya"):
    print(driver.title)
    usernameInput = driver.find_element(By.XPATH, '//*[@id="username"]') 
    passwordInput = driver.find_element(By.XPATH, '//*[@id="password"]')
    loginSubmitButton = driver.find_element(By.XPATH, '//*[@id="loginbtn"]')
    usernameInput.send_keys(loginCredentials["username"])
    passwordInput.send_keys(loginCredentials["password"])
    loginSubmitButton.click()
coursesContainerXpath = '/html/body/div[2]/div[3]/div/div/div[2]/div/section/div/section/section/div/div/div[1]/div[2]/div/div/div[1]/div/div'

coursesContainer = WebDriverWait(driver, timeout=2).until(EC.presence_of_all_elements_located((By.XPATH, coursesContainerXpath)))
coursesElmntsList = coursesContainer[0].find_elements(By.CSS_SELECTOR, "div > div > div.card-body > div > div > a")
i = 0
data["courses"] = {}
for courseElmnt in coursesElmntsList:
    courseTitle = courseElmnt.find_element(by=By.CSS_SELECTOR, value='.multiline').get_attribute("title")
    courseLink = courseElmnt.get_attribute("href")
    data["courses"][i] = {
        "title": courseTitle,
        "link": courseLink
    }
    i += 1

j = 0
for course in data["courses"]:
    driver.get(data["courses"][course]["link"])
    tmp = WebDriverWait(driver, timeout=2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[2]/nav/div/div/div[5]/div[1]/a[2]')))
    print(j)
    print(tmp)
    j += 1
