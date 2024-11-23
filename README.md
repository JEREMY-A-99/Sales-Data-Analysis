Sales Data Analysis - COMPUT 175 Assignment, University Of Alberta.
Description
This project is a Python application for analyzing sales data. It processes sales, product, and return data from CSV files, providing insights into sales performance, turnover, and transaction trends. The application is designed to answer specific business questions related to product sales, such as the top-performing products and transaction patterns.

Features
Product Data Analysis: Read and process product information, including product IDs, names, and prices.
Sales Data Analysis: Analyze sales transactions, calculate net sales, and determine the top-performing products by units sold and sales amount.
Return Data Analysis: Identify and account for returned products.
Turnover Calculation: Compute sales turnover for all products, including total units sold, sales amount, and average discounts applied.
Transaction Trends: Count the number of transactions for each day of the week.
Returned Products Report: Identify products with the highest return counts.
File Output: Write the total units sold for each product to a file for record-keeping.
Input Files
The program requires the following CSV files as input:

transactions_Products.csv: Contains product data with columns:

Product ID, Product Name, Price.
transactions_Sales.csv: Contains sales data with columns:

Transaction ID, Date (YYYY-MM-DD), Product ID, Quantity, Discount (0-1).
transactions_Returns.csv: Contains return data with columns:

Transaction ID, Return Reason.
Usage
Ensure the input files are in the same directory as the program.
Run the program using Python:
bash
Copy code
python3 sales_analysis.py
View the results printed to the console, including:
Top products by units sold and sales amount.
Sales turnover.
Transactions per weekday.
Products with the highest return counts.

Outputs
Console Output: Answers to the following questions:

The product with the largest number of units sold.
The product that generated the highest sales in dollars.
Sales turnover for all products, including average discounts.
Number of transactions per weekday.
List of returned products.
File Output: A text file named transactions_units.txt containing product IDs and their corresponding total units sold.
