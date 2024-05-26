import requests
from bs4 import BeautifulSoup
import os

# Function to scrape website
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extracting all CSS links
    css_files = [link.get('href') for link in soup.find_all('link', rel='stylesheet')]
    print('CSS Files:')
    for css in css_files:
        print(css)

    # Example: Extracting all JS links
    js_files = [script.get('src') for script in soup.find_all('script') if script.get('src')]
    print('JS Files:')
    for js in js_files:
        print(js)

    # Example: Extracting HTML content
    html_content = soup.prettify()
    print('HTML Content:')
    print(html_content[:500])  # Print the first 500 characters of HTML content

    # Save HTML content to a file
    with open('scraped_page.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Download CSS and JS files
    download_files(css_files, 'css')
    download_files(js_files, 'js')

# Function to download files
def download_files(file_urls, file_type):
    if not os.path.exists(file_type):
        os.makedirs(file_type)
    for url in file_urls:
        if not url.startswith('http'):
            url = f"{url}"
        try:
            response = requests.get(url)
            file_name = os.path.join(file_type, os.path.basename(url))
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded {file_name}')
        except Exception as e:
            print(f'Failed to download {url}: {e}')

# Prompt the user for the URL
url = input("Please enter the URL of the website you want to scrape: ")
scrape_website(url)
