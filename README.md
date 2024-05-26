# Web Scraper

This project is a Python script that scrapes a website for HTML, CSS, and JavaScript files. The script uses `requests` and `BeautifulSoup` for scraping static content.

## Prerequisites

Ensure you have Python 3 installed on your system. You will also need to install the necessary libraries listed in `requirements.txt`.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script using Python:

    ```bash
    python scrape_website.py
    ```

2. When prompted, enter the URL of the website you want to scrape.

    ```plaintext
    Please enter the URL of the website you want to scrape: https://example.com
    ```

3. The script will output the CSS and JS file links found on the page and save the HTML content to a file named `scraped_page.html`.

4. CSS and JS files will be downloaded and saved in `css` and `js` directories respectively.

## Files

- `scrape_website.py`: The main script to run the scraper.
- `requirements.txt`: The list of Python libraries required to run the script.
- `README.md`: This readme file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.