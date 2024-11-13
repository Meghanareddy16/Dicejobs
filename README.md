# Job Scraper

This project is designed to scrape job listings from Dice.com, extract job details, and save the data to a PostgreSQL database. The scraped data is also saved to a CSV file and uploaded to an S3 bucket.

## Features

- Scrapes job listings from Dice.com.
- Extracts detailed job information including title, location, date posted, work setting, work mode, job description, position ID, company name, and company URL.
- Saves the job data to a PostgreSQL database.
- Exports the job data to a CSV file.
- Uploads the CSV file to an Amazon S3 bucket.

## Requirements

- Python 3.7+
- Google Chrome browser
- Google ChromeDriver
- PostgreSQL database
- AWS account with S3 bucket

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/job-scraper.git
    cd job-scraper
    ```

2. **Install the required Python packages**:

    ```sh
    pip install -r requirements.txt
    ```


## Configuration

1. **Database Configuration**:
    Update the `insert_jobs_df_to_db` function in the code with your PostgreSQL database credentials:

    ```python
    connection = psycopg2.connect(
        user="your_db_user",          
        password="your_db_password",  
        host="your_db_host",          
        port="your_db_port",          
        database="your_db_name"       
    )
    ```

2. **AWS Configuration**:
    Update the `upload_to_s3` function with your AWS credentials:

    ```python
    aws_access_key_id = 'your_aws_access_key_id'
    aws_secret_access_key = 'your_aws_secret_access_key'
    ```

## Usage

1. **Run the scraper**:

    ```sh
    python main.py
    ```

    The script will open a Chrome browser, navigate to Dice.com, and scrape job listings. The scraped data will be saved to a CSV file, inserted into a PostgreSQL database, and uploaded to an S3 bucket.

## Functions

- `scrape_job_details(driver, wait)`: Extracts job details from the job detail page.
- `insert_jobs_df_to_db(jobs_df)`: Inserts or updates job data in the PostgreSQL database.
- `restart_driver()`: Initializes a new instance of Chrome WebDriver.
- `upload_to_s3(file_name, bucket, object_name=None)`: Uploads a file to an S3 bucket.
- `main()`: Main function that orchestrates the scraping, saving, and uploading process.

## Notes

- Ensure ChromeDriver is compatible with your version of Chrome.
- Handle your AWS credentials securely. Avoid hardcoding them in the script for production use.


## License

This project is licensed under the MIT License. See the LICENSE file for details.
