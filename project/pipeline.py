#!/usr/bin/env python3

import os
import sys

import requests
import pandas as pd
import time

# Define the URL of the dataset
dataset_url = 'https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD'

# Define the directory to save the data
data_dir = './../data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Define the paths to save the raw and cleaned data
raw_data_path = os.path.join(data_dir, 'motor_vehicle_collisions_raw.csv')
cleaned_data_path = os.path.join(data_dir, 'motor_vehicle_collisions_cleaned.csv')


def download_with_retry(url, path, retries=3, delay=5):
    """
    Downloads a file from a URL with retry logic.

    Args:
        url (str): URL of the file to download.
        path (str): Local path where the file will be saved.
        retries (int): Number of retry attempts.
        delay (int): Delay in seconds between retries.

    Raises:
        SystemExit: If the maximum number of retries is reached.
    """
    attempt = 0
    while attempt < retries:
        try:
            print(f'Downloading dataset... Attempt {attempt + 1}')
            response = requests.get(url, timeout=30)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            with open(path, 'wb') as f:
                f.write(response.content)
            print(f'Dataset downloaded and saved to {path}')
            return
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f'Download failed: {e}')
            if attempt < retries:
                print(f'Retrying in {delay} seconds...')
                time.sleep(delay)
            else:
                print('Max retries reached. Exiting.')
                raise SystemExit(e)


def handle_missing_values(df):
    """
    Handles missing values in the DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame to process.

    Returns:
        pandas.DataFrame: Processed DataFrame with missing values handled.
    """
    # Fill missing values in 'BOROUGH' with 'Unknown'
    df['BOROUGH'] = df['BOROUGH'].fillna('Unknown')

    # Fill missing 'ZIP CODE' with '00000' and convert to string
    df['ZIP CODE'] = df['ZIP CODE'].fillna('00000').astype(str)

    # Drop rows with missing latitude or longitude
    df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

    # Convert latitude and longitude to numeric
    df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce')
    df['LONGITUDE'] = pd.to_numeric(df['LONGITUDE'], errors='coerce')

    # Fill NaN values in numeric columns with zeros
    numeric_columns = [
        'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED',
        'NUMBER OF PEDESTRIANS INJURED', 'NUMBER OF PEDESTRIANS KILLED',
        'NUMBER OF CYCLIST INJURED', 'NUMBER OF CYCLIST KILLED',
        'NUMBER OF MOTORIST INJURED', 'NUMBER OF MOTORIST KILLED'
    ]
    df[numeric_columns] = df[numeric_columns].fillna(0).astype(int)

    return df


def pipeline():
    """
    Main function to execute the data pipeline.
    """
    # Download the dataset with retry logic
    download_with_retry(dataset_url, raw_data_path, retries=3, delay=5)

    # Load the dataset into a pandas DataFrame
    print('Loading dataset into DataFrame...')
    df = pd.read_csv(raw_data_path)
    validate_data(df)

    print('Identifying columns with null values...')
    null_columns = df.columns[df.isnull().any()]
    print('Columns with null values:', null_columns.tolist())

    # Optionally, print the number of null values per column
    print('\nNumber of null values per column:')
    print(df.isnull().sum())

    # Data Cleaning and Transformation
    print('Cleaning and transforming data...')

    # Convert 'CRASH DATE' and 'CRASH TIME' to datetime
    df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], errors='coerce')
    df['CRASH TIME'] = pd.to_datetime(df['CRASH TIME'], format='%H:%M', errors='coerce').dt.time

    # Handle missing values
    df = handle_missing_values(df)

    # Save the cleaned data
    df.to_csv(cleaned_data_path, index=False)
    print(f'Cleaned data saved to {cleaned_data_path}')
    os.remove(raw_data_path)


def validate_data(df):
    if df.empty:
        print('DataFrame is empty after loading data.')
        sys.exit(1)
    if df.isnull().sum().sum() > 0:
        print('DataFrame contains null values.')
    # Additional validation checks...


if __name__ == '__main__':
    pipeline()
