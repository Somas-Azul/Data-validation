# Data Validation and Cleaning Script

This Python script automates the cleaning and validation of data using Pandas and regular expressions.

# Features:

*   Validates email addresses.
*   Validates phone numbers.
*   Removes duplicate rows.
*   Handles missing values (fills with empty strings).
*   Converts date to datetime objects (if 'date' column exists).

# How to Use:

1.  Clone this repository.
2.  Install the required library: 'pip install pandas'
3.  Place your input data file (CSV) named 'input_data.csv' in the same directory as the script.
4.  Run the script: 'python data_validation.py'
5.  The cleaned data will be saved to 'cleaned_data.csv'.

# Example Input Data (input_data.csv):

```csv
name,email,phone,date
John Doe,[email address removed],+15551234567,2024-08-15
Jane Smith,[email address removed],5551234567,2024-08-15
John Doe,[email address removed],+15551234567,2024-08-15  <-- Duplicate
Invalid Email,invalid.email,,,
Missing Phone,[email address removed],+1555,2024-08-16
,[email address removed],+15559876543,2024-08-17
Test User,[email address removed],+15551112222,invalid date
