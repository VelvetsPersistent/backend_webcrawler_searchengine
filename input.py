# def get_website_url():
# Replace the URL below with the website you want to crawl
# return "http://books.toscrape.com/"
# return "https://college.vac.edu.np/"

import os


def get_user_input():
    website_url = input("Enter the URL of the website to crawl: ")
    search_query = input("Enter search query: ")

    # Call crawl.py and search.py with the user input
    os.system(f"python crawl.py {website_url}")
    os.system(f"python search.py {search_query}")


if __name__ == "__main__":
    get_user_input()
