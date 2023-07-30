
import os
import requests
from bs4 import BeautifulSoup
import csv
import sys


def get_all_urls(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags (links) on the page
    links = soup.find_all('a')

    # Extract the URLs and titles from the links
    urls_titles = [(link.get('href'), link.get_text()) for link in links]

    # Filter out None and empty URLs
    urls_titles = [(url, title)
                   for url, title in urls_titles if url and not url.startswith('#')]

    return urls_titles


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the URL of the website to crawl as a command-line argument.")
        sys.exit(1)

    website_url = sys.argv[1]
    urls_titles = get_all_urls(website_url)

    if urls_titles:
        print("\nWebpages in the website:")
        for i, (url, title) in enumerate(urls_titles, 1):
            print(f"{i}. URL: {url}")
            print(f"Title: {title}\n")

        # Create the 'datas' folder if it doesn't exist
        data_folder = 'datas'
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        csv_filepath = os.path.join(data_folder, 'webpages.csv')
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['URL', 'Title'])
            writer.writerows(urls_titles)

        print(f"\nData saved to '{csv_filepath}' inside the 'datas' folder.")
    else:
        print("No webpages found on the website.")
