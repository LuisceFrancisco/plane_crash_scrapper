
# Aviation Accident Data Scraper

This repository contains a Python script designed to scrape and compile aviation accident details from the website [Plane Crash Info](https://www.planecrashinfo.com). The script fetches accident data from 1920 to 2024 and saves it into a CSV file for easy analysis and reference.

## Features
- **Dynamic Data Extraction**: The script dynamically extracts accident details for each year and page on the website.
- **Data Cleaning**: It cleans the extracted text to remove unwanted characters and ensures the data is well-formatted for CSV output.
- **CSV Export**: The collected data is saved into a CSV file, making it convenient for further processing or analysis.

## Requirements
- Python 3.x
- `requests`
- `BeautifulSoup4`
- `csv`
- `re`

## How to Use
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/aviation-accident-data-scraper.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd aviation-accident-data-scraper
   ```
3. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the script**:
   ```bash
   python scrape_aviation_data.py
   ```

## Script Overview

- **clean_text(text)**: Cleans the text by removing unwanted characters and replacing multiple spaces with a single space.
- **get_accident_details(year, page)**: Fetches accident details for a specific year and page from the website.
- **save_to_csv(data, filename)**: Saves the collected data into a CSV file.

## Example Usage

The script scrapes accident data for years ranging from 1920 to 2024 and compiles all the details into a single CSV file named `accident_details_compiled.csv`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!
