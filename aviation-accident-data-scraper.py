import requests
from bs4 import BeautifulSoup
import csv
import re

def clean_text(text):
    """
    Remove unwanted characters and clean the text.
    Replace multiple spaces with a single space.
    Ensure semicolons do not cause issues in CSV.
    """
    cleaned_text = text.replace('\xa0', ' ').replace('\n', ' ').strip()
    cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
    cleaned_text = cleaned_text.replace(';', ',')
    return cleaned_text

def get_accident_details(year, page):
    """
    Fetch accident details from a specific page for a given year.
    """
    url = f"https://www.planecrashinfo.com/{year}/{year}-{page}.htm"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract accident details dynamically
    accident_details = {}

    rows = soup.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            key_tag = cells[0].find('b')
            if key_tag:
                key = clean_text(key_tag.get_text(separator=" ").strip().strip(":"))
                value = clean_text(cells[1].get_text(separator=" ").strip())
                accident_details[key] = value

    # Check if details are populated (to skip empty pages)
    if all(value == "" for value in accident_details.values()):
        return None

    return accident_details

def save_to_csv(data, filename):
    """
    Save the collected data to a CSV file.
    """
    if not data:
        return

    # Extract keys from the first dictionary as the header
    keys = data[0].keys()

    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys, quoting=csv.QUOTE_ALL)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Example usage
years = range(1920, 2025)  # List of years to scrape
all_details = []
output_filename = 'accident_details_compiled.csv'

for year in years:
    page = 1
    while True:
        details = get_accident_details(year, page)
        if details:
            all_details.append(details)
            print(f"Record added: {year}-{page}")
            page += 1
        else:
            break  # Stop if no more details are found

# Save all details to a single CSV file
save_to_csv(all_details, output_filename)

print(f"All accident details saved to {output_filename}")