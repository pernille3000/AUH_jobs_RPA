from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    # Launch Chrome with the specified options
    driver = webdriver.Chrome()

    # Åbn hjemmesiden
    url = "https://midtjob.dk/ledige-jobs"
    
    # Åbn en Chrome-browser ved hjælp af Selenium
    driver.get(url)
    
    # Find titel-elementet ved hjælp af XPath
    titel = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[3]/div[3]/div[2]/div[1]/a")
    print(titel.text)

    # Luk browseren
    driver.quit()

if __name__ == "__main__":
    main()
