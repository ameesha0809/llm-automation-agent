import os
import re

DATA_DIR = "/data"
EMAIL_FILE = os.path.join(DATA_DIR, "email.txt")
OUTPUT_FILE = os.path.join(DATA_DIR, "email-sender.txt")

def extract_email_regex(content):
    """Extract the sender's email using regex."""
    match = re.search(r"From:\s*.*?(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)", content, re.IGNORECASE)
    return match.group(1) if match else None

def main():
    """Read email content, extract sender's email, and save it to a file."""
    if not os.path.exists(EMAIL_FILE):
        print(f"Error: {EMAIL_FILE} not found.")
        return

    with open(EMAIL_FILE, "r", encoding="utf-8") as file:
        email_content = file.read()

    sender_email = extract_email_regex(email_content)

    if sender_email:
        print("Extracted email:", sender_email)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(sender_email)
        print(f"Sender's email saved to {OUTPUT_FILE}")
    else:
        print("No valid email found.")

if __name__ == "__main__":
    main()
