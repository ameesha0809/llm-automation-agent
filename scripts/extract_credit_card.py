import pytesseract
from PIL import Image
import re
import os
def extract_credit_card(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(img)
    
    # Extract only digits (Credit Card Number)
    card_number = "".join(re.findall(r'\d+', extracted_text))

    return card_number

def main():
    image_path = os.path.join("..", "data", "credit_card.png")  # Adjust the path
    output_path = os.path.join("..", "data", "credit_card.txt")  # Adjust the path

    # Extract card number
    card_number = extract_credit_card(image_path)

    if card_number:
        # Save to file
        with open(output_path, "w") as f:
            f.write(card_number)
        print(f"Extracted credit card number saved to {output_path}")
    else:
        print("No credit card number detected.")

if __name__ == "__main__":
    main()
