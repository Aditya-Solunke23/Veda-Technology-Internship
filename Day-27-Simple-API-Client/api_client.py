"""
Day 27 - Simple API Client
Fetches data from a public REST API and displays it
in a readable format.
"""

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts(limit=5):
    """Fetch a limited number of posts from the public API."""
    try:
        print("\nConnecting to the API...")
        response = requests.get(
            API_URL,
            params={"_limit": limit},
            timeout=10
        )

        # Raise an exception for unsuccessful HTTP responses.
        response.raise_for_status()

        # Convert the JSON response into Python data.
        posts = response.json()

        if not isinstance(posts, list):
            print("Error: Unexpected API response format.")
            return None

        print("API request successful!")
        print(f"HTTP Status Code: {response.status_code}")

        return posts

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request Error: {error}")

    except ValueError:
        print("Error: The API returned invalid JSON data.")

    return None


def display_posts(posts):
    """Display the retrieved posts in a readable format."""
    if not posts:
        print("\nNo posts available to display.")
        return

    print("\n" + "=" * 60)
    print("              PUBLIC API CLIENT")
    print("=" * 60)

    for post in posts:
        print(f"\nPost ID : {post.get('id', 'N/A')}")
        print(f"User ID : {post.get('userId', 'N/A')}")
        print(f"Title   : {post.get('title', 'N/A')}")
        print(f"Body    : {post.get('body', 'N/A')}")
        print("-" * 60)

    print(f"\nTotal posts displayed: {len(posts)}")


def main():
    """Run the API client application."""
    print("=" * 60)
    print("                 SIMPLE API CLIENT")
    print("=" * 60)

    while True:
        user_input = input(
            "\nHow many posts would you like to fetch? (1-10, or 0 to exit): "
        ).strip()

        try:
            limit = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if limit == 0:
            print("Thank you for using the Simple API Client!")
            break

        if not 1 <= limit <= 10:
            print("Please enter a number between 1 and 10, or 0 to exit.")
            continue

        posts = fetch_posts(limit)

        if posts is not None:
            display_posts(posts)


if __name__ == "__main__":
    main()