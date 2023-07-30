import os
import csv
import sys


def search_webpages(search_query):
    data_folder = 'datas'
    csv_filepath = os.path.join(data_folder, 'webpages.csv')

    if not os.path.exists(csv_filepath):
        print("No data found. Please run 'crawl.py' first to generate the data.")
        return

    with open(csv_filepath, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        found_results = []
        for row in reader:
            url, title = row
            if search_query.lower() in title.lower():
                found_results.append((url, title))

        if found_results:
            print("\nSearch Results:")
            for i, (url, title) in enumerate(found_results, 1):
                print(f"{i}. URL: {url}")
                print(f"   Title: {title}\n")
        else:
            print("No matching results found.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the search query as a command-line argument.")
        sys.exit(1)

    search_query = sys.argv[1]
    search_webpages(search_query)
