from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

def main():
    # Launch Chrome
    driver = webdriver.Chrome()

    # Open the website
    url = "https://midtjob.dk/ledige-jobs"
    driver.get(url)

    try:
        # Find the table element by class name
        table_element = driver.find_element(By.CLASS_NAME, 'css_jobsAdvTable')

        # Extract the outer HTML content of the table element
        table_html = table_element.get_attribute('outerHTML')
        print(table_html)
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(table_html, 'html.parser')

        # Find all table rows and extract data
        rows = soup.find_all('div')
        
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [col.get_text(strip=True) for col in cols]
            data.append(cols)

        # Create DataFrame from extracted data
        df = pd.DataFrame(data, columns=['Firm Name', 'Last Name', 'First Name'])

        # Print DataFrame
        print("DataFrame from extracted table data:")
        print(df)

    except Exception as e:
        print("Error occurred:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
