"""
Day 29 - Web Scraping Program
Extracts book information from a practice website
and saves the results to a CSV file.
"""

import csv
import requests
from bs4 import BeautifulSoup


URL = "https://books.toscrape.com/"
OUTPUT_FILE = "scraped_books.csv"


def fetch_page(url):
    """Fetch webpage HTML using an HTTP GET request."""
    try:
        headers = {
            "User-Agent": "PythonWebScraper/1.0 (educational project)"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()
        return response.text

    except requests.exceptions.Timeout:
        print("Error: The website took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the website.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request error: {error}")

    return None


def extract_books(html):
    """Extract book titles, prices, ratings, and availability."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title_element = book.select_one("h3 a")
        price_element = book.select_one(".price_color")
        availability_element = book.select_one(".availability")
        rating_element = book.select_one("p.star-rating")

        if not title_element or not price_element:
            continue

        rating = "Unknown"

        if rating_element:
            rating_classes = rating_element.get("class", [])

            for rating_name in ["One", "Two", "Three", "Four", "Five"]:
                if rating_name in rating_classes:
                    rating = rating_name
                    break

        books.append({
            "title": title_element.get("title", "").strip(),
            "price": price_element.get_text(strip=True),
            "rating": rating,
            "availability": (
                availability_element.get_text(" ", strip=True)
                if availability_element
                else "Unknown"
            ),
        })

    return books


def save_to_csv(books, filename):
    """Save extracted book information to a CSV file."""
    if not books:
        print("No book records found. CSV file was not created.")
        return False

    fieldnames = [
        "title",
        "price",
        "rating",
        "availability"
    ]

    try:
        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as csv_file:

            writer = csv.DictWriter(
                csv_file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(books)

        print(f"Data saved successfully to: {filename}")
        return True

    except OSError as error:
        print(f"Error saving CSV file: {error}")
        return False


def main():
    """Run the web scraping application."""
    print("=" * 55)
    print("              WEB SCRAPING PROGRAM")
    print("=" * 55)

    print(f"Website: {URL}")
    print("\nFetching webpage...")

    html = fetch_page(URL)

    if html is None:
        print("Unable to retrieve webpage data.")
        return

    print("Webpage retrieved successfully.")

    print("\nExtracting book information...")
    books = extract_books(html)

    if not books:
        print("No books were found on the webpage.")
        return

    print(f"Total books extracted: {len(books)}")

    print("\nSample extracted records:")
    print("-" * 55)

    for book in books[:5]:
        print(f"Title        : {book['title']}")
        print(f"Price        : {book['price']}")
        print(f"Rating       : {book['rating']}")
        print(f"Availability : {book['availability']}")
        print("-" * 55)

    save_to_csv(books, OUTPUT_FILE)


if __name__ == "__main__":
    main()