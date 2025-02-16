import os
import json
import re

DATA_DIR = "/data/docs/"
OUTPUT_FILE = "/data/docs/index.json"

def get_first_h1(content):
    """Extract the first H1 from Markdown content."""
    match = re.search(r"^# (.+)", content, re.MULTILINE)
    return match.group(1) if match else None

def process_markdown_files():
    """Find all Markdown files and extract titles without using API."""
    index = {}

    for root, _, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, DATA_DIR)  # Get relative path

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                title = get_first_h1(content)
                if title:  # Only store if H1 is found
                    index[relative_path] = title

    # Save results to index.json
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=4)

    print("Index file created:", OUTPUT_FILE)

# Run the function
process_markdown_files()
