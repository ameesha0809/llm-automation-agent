from datetime import datetime

input_file = "/data/dates.txt"
output_file = "/data/dates-wednesdays.txt"

date_formats = ["%Y-%m-%d", "%b %d, %Y", "%B %d, %Y"]  # Supports "2009-01-17", "Jan 17, 2009", "January 17, 2009"

def parse_date(date_str):
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None  # Return None if no format matches

try:
    with open(input_file, "r") as f:
        dates = f.readlines()

    wednesday_count = sum(1 for date in dates if parse_date(date) and parse_date(date).weekday() == 2)

    with open(output_file, "w") as f:
        f.write(str(wednesday_count) + "\n")

    print(f"Successfully counted {wednesday_count} Wednesdays and saved to {output_file}")

except Exception as e:
    print(f"Error: {e}")
