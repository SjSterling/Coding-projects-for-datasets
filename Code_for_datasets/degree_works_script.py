import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv


class MySpider(scrapy.Spider):
    name = 'data'
    start_urls = ['https://degreeworks.valdosta.edu/worksheets/WEB31']

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.site_info = SiteInfo()
        self.driver_path = "/Users/ster/Downloads/chromedriver-mac-arm64 3"
        self.driver = None
        self.extracted_data = []  # Initialize the extracted_data attribute as an empty list

        # List of XPath expressions for tables you want to scrape
        self.table_xpaths = [
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[4]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[5]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[6]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[7]/div/div/div["
            "2]/div/div/div/div/div/div[1]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[8]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[9]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[10]/div/div/div["
            "2]/div/div/div/div/div/div[1]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[11]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[12]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[13]/div/div/div["
            "2]/div/div/div/div/div/div[1]/table/tbody",
            "/html/body/div/div/div[2]/div/main/div/div[3]/div/div[2]/div/div/div[14]/div/div/div["
            "2]/div/div/div/div/div/div[2]/table/tbody"
        ]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_data)

    def parse_data(self, response):
        # Your scraping logic here
        if not self.driver:
            self.login()

        for table_xpath in self.table_xpaths:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, table_xpath))
                )

                # Find the table body using the provided XPath
                table_body = self.driver.find_element(By.XPATH, table_xpath)

                # Get rows of the table
                rows = table_body.find_elements(By.TAG_NAME, "tr")

                for row in rows:
                    # Extract data from each column in the row
                    columns = row.find_elements(By.XPATH, ".//td | .//th")
                    data_columns = [col.text for col in columns]  # Extract data from all columns
                    data_columns = [data.strip() for data in data_columns if data.strip()]  # Filter out empty data

                    if data_columns:  # Ensure that there is at least one column with data
                        # Check each column for SVG elements
                        status = "N/A"
                        for column in columns:
                            svg_elements = column.find_elements(By.XPATH, ".//*[local-name()='svg']")
                            if svg_elements:
                                svg_class = svg_elements[0].get_attribute("class")
                                if "ds-check-feedback" in svg_class:  # The class name for complete
                                    status = "complete"
                                elif "ds-circle" in svg_class:  # The class name for incomplete
                                    status = "incomplete"
                                elif "ds-icon ds-partial" in svg_class:  # The class name for partially complete
                                    status = "partially complete"
                                break  # Break the loop if an SVG element is found in the column

                        self.extracted_data.append((data_columns, status))  # Append the data and status to the list

            except TimeoutException:
                self.logger.warning("Timeout waiting for the table body element.")
                continue

    def login(self):
        try:
            service = Service(executable_path=self.driver_path)
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
            options.add_argument("--disable-gpu")  # Disable GPU to improve performance
            options.add_argument("--disable-extensions")  # Disable extensions for faster loading
            options.add_argument("--disable-infobars")  # Disable infobars for faster loading
            options.add_argument("--disable-images")  # Disable loading images
            options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            self.driver = webdriver.Chrome(service=service, options=options)

            self.driver.get(self.site_info.login_url)

            username = input("Enter your username: ")
            password = input("Enter your password: ")

            username_box = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, self.site_info.username_id)))
            password_box = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, self.site_info.password_id)))

            username_box.send_keys(username)
            password_box.send_keys(password)

            login_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, self.site_info.login_button_id)))
            login_button.click()

            success_url_prefix = "https://degreeworks.valdosta.edu/"
            WebDriverWait(self.driver, 20).until(UrlStartsWith(success_url_prefix))

            if self.driver.current_url.startswith(success_url_prefix):
                print('Login successful for {}'.format(self.site_info.login_url))
                return True
            else:
                print('Login failed for {}'.format(self.site_info.login_url))
                return False

        except Exception as e:
            print('Failed to login: Message: {}'.format(str(e)))
            return False

    def closed(self, reason):
        # Save the extracted data to a text file
        with open("coolbody.csv", "w", encoding="utf-8") as txtfile:
            for item in self.extracted_data:
                txtfile.write(f"Data Columns: {item[0]}, Status: {item[1]}\n")

        print("Extracted data saved to extracted_data.txt file.")

class SiteInfo:
    def __init__(self):
        self.login_url = "https://degreeworks.valdosta.edu/worksheets/WEB31"
        self.username_id = "userNameInput"
        self.password_id = "passwordInput"
        self.login_button_id = "submitButton"
        self.username = "sjscarlett@valdosta.edu"  # Replace with your actual username
        self.password = "GAkings03!"  # Replace with your actual password


class UrlStartsWith:
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, driver):
        return driver.current_url.startswith(self.prefix)


# Run the spider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(MySpider)
process.start()
