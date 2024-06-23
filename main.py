from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def main():
    # Launch Chrome and open the website
    driver = webdriver.Chrome()
    url = "https://midtjob.dk/ledige-jobs"
    driver.get(url)

    try:
        while True:
            try:
                # Find the "vis flere jobs" button and click on it
                vis_flere_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[3]/a')
                vis_flere_button.click()
                time.sleep(2)  # Adjust the sleep time as needed
            except:
                # Break the loop if the button is no longer visible
                break
    
        # Get the page source and parse it with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all job rows
        job_rows = soup.find_all('div', class_='css_jobsAdvRow')

        # Extract all column names from the first row
        first_row = job_rows[0]
        column_names = [cell.get_text(strip=True) for cell in first_row.find_all('div', class_='css_jobsAdvCell')[:-1]]

        # Extract data from each job row
        data = []
        for row in job_rows[1:]:
            cells = row.find_all('div', class_='css_jobsAdvCell')[:-1]
            row_data = [cell.get_text(strip=True) for cell in cells]
            # Remove column names from cell values
            for i, cell_value in enumerate(row_data):
                for col_name in column_names: 
                    row_data[i] = row_data[i].replace(col_name, '').strip()
            data.append(row_data)

        # Create DataFrame from extracted data
        df = pd.DataFrame(data, columns = column_names)

        # Export to excel
        df.to_excel("job_listings.xlsx", index=False) 

        # Print DataFrame
        print("DataFrame exported to excel from extracted table data")
        
    except Exception as e:
        print("Error occurred:", str(e))

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
