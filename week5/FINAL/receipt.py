# W05 Project: Grocery Store Receipt Generator
# 
# This program reads product and order data from CSV files,
# processes the data, and prints a formatted receipt.
# 
# Features:
# - Handles exceptions for missing or inaccessible files (FileNotFoundError, PermissionError)
# - Detects and reports unknown product IDs (KeyError)
# - Calculates subtotal, sales tax (6%), and total
# - Displays the current date and time
# - Shows days remaining until New Year's Sale
# - Prints a "return by" date (30 days from purchase)
# 
# Enhancements Beyond Requirements:
# - More detailed error messages for debugging
# - Dynamic return policy date printed on the receipt
# - Future event notification (New Year's Sale countdown)

import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row  # Store the whole row as value
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
        exit()
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
        exit()
    
    return dictionary

def main():
    """Main function to process the receipt printing."""
    STORE_NAME = "Inkom Emporium"
    SALES_TAX_RATE = 0.06
    products_filename = "products.csv"
    request_filename = "request.csv"
    
    products_dict = read_dictionary(products_filename, 0)
    print(STORE_NAME)
    
    total_items = 0
    subtotal = 0
    try:
        with open(request_filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            
            print("\nRequested Items")
            for row in reader:
                product_number, quantity = row[0], int(row[1])
                if product_number not in products_dict:
                    raise KeyError(f"Unknown product ID: {product_number}")
                
                product_name = products_dict[product_number][1]
                product_price = float(products_dict[product_number][2])
                
                print(f"{product_name}: {quantity} @ {product_price:.2f}")
                total_items += quantity
                subtotal += quantity * product_price
    
        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax
        
        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")
        
        current_datetime = datetime.now()
        print(current_datetime.strftime("%a %b %d %I:%M:%S %Y"))
        
        # Additional Features
        new_year = datetime(current_datetime.year + 1, 1, 1)
        days_until_sale = (new_year - current_datetime).days
        print(f"New Year's Sale starts in {days_until_sale} days!")
        
        return_date = current_datetime + timedelta(days=30)
        print(f"Return by: {return_date.strftime('%a %b %d %I:%M %p %Y')}")
    
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file\n{e}")
    
if __name__ == "__main__":
    main()
