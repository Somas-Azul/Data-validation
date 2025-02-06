import pandas as pd
import re

def validate_email(email):
    if not isinstance(email, str) or not email:  # Handle non-string or empty values
        return False
    email_regex = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    if not isinstance(phone, str) or not phone: # Handle non-string or empty values
        return False
    phone_regex = r"^\+?[1-9]\d{1,14}$"  # International phone number regex (adapt if needed)
    return re.match(phone_regex, phone) is not None

def clean_data(df):
    # Email Validation
    df['email_valid'] = df['email'].apply(validate_email)
    df = df[df['email_valid']]  # Keep only valid emails
    df.drop(columns=['email_valid'], inplace=True)

    # Phone Validation
    df['phone_valid'] = df['phone'].apply(validate_phone)
    df = df[df['phone_valid']]  # Keep only valid phone numbers
    df.drop(columns=['phone_valid'], inplace=True)

    # Remove Duplicates
    df.drop_duplicates(inplace=True)

    # Handle Missing Values (Example: Fill with "")
    df.fillna("", inplace=True)

    # Convert Data Types (Example: Date)
    if 'date' in df.columns: #check for column before converting
      df['date'] = pd.to_datetime(df['date'], errors='coerce') #errors='coerce' will set invalid dates to NaT

    return df

# Example Usage
input_file = "input_data.csv"
output_file = "cleaned_data.csv"

try:
    df = pd.read_csv(input_file)
    cleaned_df = clean_data(df)
    cleaned_df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
