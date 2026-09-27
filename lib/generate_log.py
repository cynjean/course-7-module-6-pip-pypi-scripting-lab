"""Generate a dated text log, with an optional API-backed CLI example."""

import argparse
from datetime import datetime


def generate_log(data):
    """Write a list of entries to today's log file and return its filename."""
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    # Writing an empty list still creates a valid, empty log file.
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_post():
    """Fetch one sample post using the third-party Requests package."""
    import requests

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def main():
    """Run the log generator from the command line."""
    parser = argparse.ArgumentParser(description="Write a dated activity log.")
    parser.add_argument(
        "--fetch-post",
        action="store_true",
        help="fetch a sample post and write its title to the log",
    )
    args = parser.parse_args()

    log_data = ["User logged in", "User updated profile", "Report exported"]
    if args.fetch_post:
        post = fetch_post()
        log_data = [f"Fetched post {post.get('id', 'unknown')}: {post.get('title', 'No title found')}"]

    generate_log(log_data)


if __name__ == "__main__":
    main()
