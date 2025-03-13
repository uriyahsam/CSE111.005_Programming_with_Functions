import csv

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
    
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row  # Store the whole row as value
    
    return dictionary

def main():
    """Main function to process the receipt printing."""
    products_filename = "products.csv"
    request_filename = "request.csv"
    
    products_dict = read_dictionary(products_filename, 0)
    print("All Products")
    print(products_dict)
    
    with open(request_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        print("\nRequested Items")
        for row in reader:
            product_number, quantity = row[0], int(row[1])
            product_name = products_dict[product_number][1]
            product_price = float(products_dict[product_number][2])
            print(f"{product_name}: {quantity} @ {product_price:.2f}")

if __name__ == "__main__":
    main()