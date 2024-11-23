"""
----------------------------------------------------
 COMPUT 175 ASSIGNMENT 1
University of Alberta
 Author: Jeremy Ajoku
 Sales Data Analysis

----------------------------------------------------
"""
import datetime # imports datetime module

def read_product_data(file_path):
    """
    Read product data from a CSV file and return a dictionary 
    """
    product_data = {}
    with open(file_path, 'r') as products_file:
        products_file.readline()  
        for line in products_file:
            product_id, product_name, price = line.strip().split(',')
            product_data[product_id] = {'name': product_name, 'price': float(price)}
    return product_data
def read_sales_data(file_path):
    """
    Read sales data from a CSV file and return a dictionary 
    """
    sales_data = {}
    with open(file_path, 'r') as sales_file:
        sales_file.readline()  
        for line in sales_file:
            transaction_id, date, product_id, quantity, discount = line.strip().split(',')
            quantity = int(quantity)
            sales_data[transaction_id] = (date, product_id, quantity, discount)
    return sales_data

def read_return_data(file_path):
    """
    Read return data from a CSV file and return a set of transaction IDs.
    """
    return_data = set()
    with open(file_path, 'r') as return_file:
        return_file.readline() 
        # this literates through eaach line in the file
        for line in return_file:
            transaction_id, _ = line.strip().split(',')
            return_data.add(transaction_id)
    return return_data # returns the set containing transaction IDs


def calculate_sales_amount(sales_data, product_data, return_data):
    """
    Calculate total sales amount for each product after returns.
    """
    sales_amount = {}
    for transaction_id, (date, product_id, quantity, discount) in sales_data.items():
        
        # Check if the transaction is not a return
        if transaction_id not in return_data:
            price = product_data[product_id]['price']
            # this calculates the sales amount for the product and add it to the dictionary
            sales_amount[product_id] = sales_amount.get(product_id, 0) + (price * quantity * (1-float(discount)))
    return sales_amount

def calculate_net_sales(sales_data, return_data):
    """
    Calculate net sales (units sold after returns) from sales data and return as a dictionary.
    """
    net_sales = {}
    for transaction_id, (date, product_id, quantity, discount) in sales_data.items():
        if transaction_id not in return_data:
            net_sales[product_id] = net_sales.get(product_id, 0) + quantity
    return net_sales

def get_top_n_products(net_sales, n=3):
    """
    Get the top N products with the highest net sales and return as a sorted list.
    """
    max_sales_product_ids = sorted(net_sales, key=net_sales.get, reverse=True)[:n]
    return max_sales_product_ids

def print_top_products(product_data, sorted_product_ids, net_sales):
    """
    Print the top products with their corresponding units sold.
    """
    
    for product_id in sorted_product_ids:
        product_info = product_data.get(product_id)
        if product_info is not None:
            product_name = product_info['name']
        else:
            product_name = "Unknown Product"
        units_sold = net_sales.get(product_id, 0)
        print("{:<20} {:>3}".format(product_name, units_sold))
        
        
def print_top_products_units(product_data, sorted_product_ids, net_sales):
    """
    Print the top products with their corresponding units sold.
    """
    
    for product_id in sorted_product_ids:
        product_info = product_data.get(product_id)
        if product_info is not None:
            product_name = product_info['name']
        else:
            product_name = "Unknown Product"
        units_sold = net_sales.get(product_id, 0)
        print("{:<20} {:>3}".format(product_name, units_sold))

def print_top_products_amount(product_data, sorted_product_ids, sales_amount):
    """
    Print the top products with their corresponding sales amount.
    """
    print("{:<20} {:>10}".format("Product Name", "Sales Amount"))
    
    for product_id in sorted_product_ids:
        product_info = product_data.get(product_id)
        if product_info is not None:
            product_name = product_info['name']
        else:
            product_name = "Unknown Product"
        amount = sales_amount.get(product_id, 0)
        print("{:<20} ${:>9,.2f}".format(product_name, amount))
        
def all_sales_turnover(sales_data, return_data, product_data):
    """
    Calculate the turnover for all sales.
    """
    turnover_data = []

    # Loop through each product in the product data
    for product_id, product_info in product_data.items():
        total_units = 0
        total_sales = 0
        total_discounted = 0
        total_discount_given = 0

        # Loop through each transaction in the sales data
        for transaction_id, (date, sale_product_id, quantity, discount) in sales_data.items():
            # this checks if the product in the transaction matches the current product and if it's not a return
            if sale_product_id == product_id and transaction_id not in return_data:
                price_per_unit = product_info['price']
                total_units += quantity
                total_discount_given += float(discount)
                
                # Calculate total sales amount and total discounted amount
                total_sales += price_per_unit * quantity * (1 - float(discount))
                total_discounted += price_per_unit * quantity * float(discount)

        # calculates average discount
        if total_sales + total_discounted > 0:
            average_discount = 100 * total_discounted / (total_sales + total_discounted)
        else:
            average_discount = 0

        # append turnover data for the current product
        turnover_data.append((product_id, product_info['name'], total_units, total_sales, average_discount, total_discounted))
 
    # Sort turnover data based on total discounted amount in descending order
    sorted_turnover = sorted(turnover_data, key=lambda x: x[5], reverse=True)

    return sorted_turnover

def print_turnover_table(turnover_data):
    """
    Print the turnover table.
    """
    # Print the table header
    print("+---+--------------------+---+-----------+------+-------------+")
    # Loop through each tuple in turnover_data and print the data formatted in a table
    for product_id, product_name, units_sold, sales_amount, avg_discount, total_discount in turnover_data:
        # Format and print each row of the table
        print("|{:<3}|{:>20}|{:>3}|${:>11,.2f}|{:>5.2f}%|${:>11,.2f}|".format(product_id, product_name[:20], units_sold, sales_amount, avg_discount, total_discount))
    # Print the table footer
    print("+---+--------------------+---+-----------+------+-------------+")
    
    
# Function to count transactions per weekday
def count_transactions_per_weekday(sales_file_path):
    """
    Counts the number of sales transactions per weekday.
    """
    # Initialize a dictionary to store the count of transactions for each weekday
    transactions_per_weekday = {
        'Monday': 0,
        'Tuesday': 0,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0
    }
    # Open the sales file
    with open(sales_file_path, 'r') as sales_file:
        next(sales_file)  # skip header
        # this literate through each line in the sales file
        for line in sales_file:
            # this extracts the transaction date from the line and convert it to a datetime object
            transaction_date = datetime.datetime.strptime(line.strip().split(',')[1], "%Y-%m-%d")
            # Gets the weekday from the transaction date and increment the corresponding count 
            weekday = transaction_date.strftime("%A")
            transactions_per_weekday[weekday] += 1
    # Return the dictionary containing the count of transactions for each weekday
    return transactions_per_weekday


def print_transactions_per_weekday(transactions_per_weekday):
    """
    Prints the number of sales transactions per weekday.
    """
    
    for weekday, count in transactions_per_weekday.items():
        print(f"{weekday:9}:{count:3}")

def count_returned_products(return_data, sales_data):
    """
    Count the number of times each product was returned.
    """
    returned_products = {}
    for transaction_id in return_data:
        product_id = sales_data[transaction_id][1]  # Get the product ID from sales data
        returned_products[product_id] = returned_products.get(product_id, 0) + 1
    return returned_products

def print_returned_products(product_data, returned_products):
    """
    Print the list of returned products without sorting,
    along with the number of times they were returned.
    """
    # this literate through each returned product and print its details
    for product_id, count in returned_products.items():
        # this gets the product name from the product data dictionary
        product_name = product_data.get(product_id, {}).get('name', 'Unknown Product')
        # this prints the  product id, name, and count of returns
        print(f"{product_id:3} {product_name:20} {count:3}")  
        
def write_units_sold_to_file(product_data, net_sales):
    """
    Write each line with the product ID and corresponding total units sold to a text file.
    """
    with open("transactions_units.txt", "w") as file:
        for product_id, units_sold in net_sales.items():
            file.write(f"{product_id},{units_sold}\n")
        
def main():
    # this reads the  sales data
    sales_data = read_sales_data('transactions_Sales.csv')

    # this reads the  return data
    return_data = read_return_data('transactions_Returns.csv')

    # this reads the product data
    product_data = read_product_data('transactions_Products.csv')

    # this calculates the net sales
    net_sales = calculate_net_sales(sales_data, return_data)

    # this calculates the sales amount
    sales_amount = calculate_sales_amount(sales_data, product_data, return_data)

    # this helps determine the top 3 products with the highest sales amount
    top_product_ids_amount = get_top_n_products(sales_amount)

    # this determines the top 3 products with the highest units sold
    top_product_ids_units = get_top_n_products(net_sales)

    # this print the top products with the highest sales amount
    print("1-What is the product that led to the larger number of sales in units?\n")
    print_top_products_units(product_data, top_product_ids_units, net_sales)
    
    print("\n2-What is the product that led to the larger number of sales in dollars?\n")
    print_top_products_amount(product_data, top_product_ids_amount, sales_amount)

    # this calculates and print turnover for all sales
    print("\n3-What is the turnover for all sales?\n")
    turnover_data = all_sales_turnover(sales_data, return_data, product_data)
    print_turnover_table(turnover_data)
    
    # this prints the number of transactions per weekday
    print("\n4-What are the number of transactions per weekday?\n")
    transactions_per_weekday = count_transactions_per_weekday("transactions_Sales.csv")
    print_transactions_per_weekday(transactions_per_weekday)
    
    # this counts and print the returned products
    print("\n5- What are the returned products?\n")
    returned_products = count_returned_products(return_data, sales_data)
    print_returned_products(product_data, returned_products)
    
    # this writes total units sold to a text file
    write_units_sold_to_file(product_data, net_sales)    


if __name__ == "__main__":
    main()