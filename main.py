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
    
        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(table_html, 'html.parser')

        # Find column names (assuming they are in the first row)
        column_names = []
        header_row = soup.find('div', class_='css_jobsAdvRow')
        if header_row:
            columns = header_row.find_all('div', class_='css_jobsAdvCell') 
            column_names = [col.get_text(strip=True) for col in columns]

        # Find all table rows containing data
        data_rows = soup.find_all('div', class_='css_jobsAdvRow')

        # Extract data from each row
        data = []
        for row in data_rows:
            cells = row.find_all('div', class_='css_jobsAdvCell')
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)

        # Create DataFrame from extracted data with dynamic column names
        df = pd.DataFrame(data, columns=column_names)

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
