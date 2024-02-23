from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

url = "https://cloudirector.github.io"  # Replace with the desired URL
output_path = "/github/workspace/screenshot.png"

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(url)
    driver.save_screenshot(output_path)
    print(f"Screenshot captured and saved as {output_path}")
finally:
    driver.quit()
