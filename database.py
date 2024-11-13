import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

def insert_jobs_df_to_db(jobs_df):
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        cursor = connection.cursor()

        for index, row in jobs_df.iterrows():
            cursor.execute("SELECT COUNT(1) FROM job_details WHERE position_id = %s", (row['position_id'],))
            if cursor.fetchone()[0]:
                postgres_update_query = """
                UPDATE job_details 
                SET title = %s, location = %s, date_posted = %s, work_setting = %s, work_mode = %s, job_description = %s, company_name = %s, company_url = %s, job_url = %s, scraped_date = %s
                WHERE position_id = %s
                """
                record_to_update = (
                    row['title'],
                    row['location'],
                    row['date_posted'],
                    row['work_setting'],
                    row['work_mode'],
                    row['job_description'],
                    row['company_name'],
                    row['company_url'],
                    row['job_url'],
                    row['scraped_date'],
                    row['position_id']
                )
                cursor.execute(postgres_update_query, record_to_update)
            else:
                postgres_insert_query = """
                INSERT INTO job_details (title, location, date_posted, work_setting, work_mode, job_description, position_id, company_name, company_url, job_url, scraped_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                record_to_insert = (
                    row['title'],
                    row['location'],
                    row['date_posted'],
                    row['work_setting'],
                    row['work_mode'],
                    row['job_description'],
                    row['position_id'],
                    row['company_name'],
                    row['company_url'],
                    row['job_url'],
                    row['scraped_date']
                )
                cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert records into job_details table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
