# Lotto Scraper

This project is a Python-based tool to fetch lottery results data from an online API and save it into a CSV file for further analysis. It leverages Python libraries like `requests` for API interaction, `csv` for data storage, and `datetime` for date manipulation.

## Features

- Fetches lottery data for a specified date range.
- Handles monthly date ranges efficiently.
- Writes results to a structured CSV file.
- Handles API errors gracefully.
- Includes a rate limiter to avoid overloading the API server.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.6 or later
- pip (Python package installer)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/lotto-scraper.git
   cd lotto-scraper
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *(Create a `requirements.txt` file if not already present with `requests` listed in it.)*

## Usage

1. Open the script `lotto_scraper.py` and ensure the date range parameters in the `main()` function are set correctly. The default configuration fetches data from January 2016 to December 2024.

2. Run the script:

   ```bash
   python lotto_scraper.py
   ```

3. The results will be saved in a CSV file named `lotto_results.csv` in the current directory.

## Configuration

### Date Range

You can configure the start and end date for fetching data by modifying the following line in the `main()` function:

```python
    date_ranges = get_monthly_date_ranges(2016, 1, 2024, 12)
```

- The first two numbers specify the start year and month.
- The last two numbers specify the end year and month.

### API Details

The script fetches data from the API endpoint:

```
https://data.api.thelott.com/sales/vmax/web/data/lotto/results/search/daterange
```

Ensure the headers and payload match the API requirements if you plan to modify the API call.

## Output

The script generates a CSV file with the following columns:

- `DrawNumber`: Unique identifier for the draw.
- `DrawDate`: Date of the draw.
- `PrimaryNumbers`: Primary lottery numbers drawn.
- `SecondaryNumbers`: Secondary or supplementary lottery numbers drawn.

Example:

| DrawNumber | DrawDate   | PrimaryNumbers       | SecondaryNumbers |
|------------|------------|----------------------|------------------|
| 3611       | 2016-02-27 | 38,3,22,18,21,5     | 27,45           |
| 3609       | 2016-02-20 | 30,5,17,22,42,26    | 19,36           |

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## Acknowledgments

- [The Lott](https://www.thelott.com) for providing the API.
- Python community for awesome libraries and support.

---

Feel free to reach out for any questions or suggestions!
https://github.com/scthakurii
