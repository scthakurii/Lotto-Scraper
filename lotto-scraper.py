import requests
import json
import csv
from datetime import datetime, timedelta
import time

def get_monthly_date_ranges(start_year, start_month, end_year, end_month):
    ranges = []
    current = datetime(start_year, start_month, 1)
    if end_month == 12:
        end = datetime(end_year + 1, 1, 1)  # Move to January of the next year
    else:
        end = datetime(end_year, end_month + 1, 1)  # Increment the month

    while current < end:
        next_month = current + timedelta(days=32)
        next_month = next_month.replace(day=1)

        start_date = current.strftime("%Y-%m-%dT16:00:00Z")
        end_date = (next_month - timedelta(days=1)).strftime("%Y-%m-%dT15:59:59Z")

        ranges.append((start_date, end_date))
        current = next_month

    return ranges

def fetch_lotto_data(start_date, end_date):
    url = 'https://data.api.thelott.com/sales/vmax/web/data/lotto/results/search/daterange'

    headers = {
        'accept': '*/*',
        'content-type': 'application/json',
        'origin': 'https://www.thelott.com',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
    }

    data = {
        "DateStart": start_date,
        "DateEnd": end_date,
        "ProductFilter": ["TattsLotto"],
        "CompanyFilter": ["NSWLotteries"]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def write_to_csv(data_list, filename='lotto_results.csv'):
    fieldnames = ['DrawNumber', 'DrawDate', 'PrimaryNumbers', 'SecondaryNumbers']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in data_list:
            writer.writerow({
                'DrawNumber': item['DrawNumber'],
                'DrawDate': item['DrawDate'],
                'PrimaryNumbers': ','.join(map(str, item['PrimaryNumbers'])),
                'SecondaryNumbers': ','.join(map(str, item['SecondaryNumbers']))
            })

def main():
    all_results = []
    date_ranges = get_monthly_date_ranges(2016, 1, 2024, 12)

    for start_date, end_date in date_ranges:
        print(f"Fetching data for period: {start_date} to {end_date}")
        response_data = fetch_lotto_data(start_date, end_date)

        if response_data and response_data.get('Success') and response_data.get('Draws'):
            all_results.extend(response_data['Draws'])

        # Be nice to the API server
        time.sleep(1)

    write_to_csv(all_results)
    print(f"Data collection complete. Total draws collected: {len(all_results)}")

if __name__ == "__main__":
    main()
