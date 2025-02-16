import sqlite3

def calculate_gold_ticket_sales(db_path):
    """Calculate the total sales for 'Gold' ticket type."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Query to sum total sales for 'Gold' tickets
        cursor.execute("SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'")
        total_sales = cursor.fetchone()[0]
        
        conn.close()
        return total_sales if total_sales else 0  # Return 0 if no data found
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    db_path = "../data/ticket-sales.db"  # Adjust path if needed
    output_path = "../data/ticket-sales-gold.txt"

    total_sales = calculate_gold_ticket_sales(db_path)

    if total_sales is not None:
        with open(output_path, "w") as f:
            f.write(str(total_sales))
        print(f"Total sales for 'Gold' tickets saved to {output_path}")
    else:
        print("Failed to calculate total sales.")

if __name__ == "__main__":
    main()
