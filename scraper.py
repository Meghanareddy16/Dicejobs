import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def scrape_job_details(driver, wait):
    job_details = {}

    # Scrape job title
    try:
        job_details['title'] = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1[data-cy='jobTitle']"))).text
    except:
        job_details['title'] = None

    # Scrape job location
    try:
        job_details['location'] = driver.find_element(By.CSS_SELECTOR, "li[data-cy='location']").text
    except:
        job_details['location'] = None

    # Scrape job posting date
    try:
        job_details['date_posted'] = driver.find_element(By.CSS_SELECTOR, "li[data-cy='postedDate'] span#timeAgo").text
    except:
        job_details['date_posted'] = None

    # Scrape work setting (e.g., remote, on-site)
    try:
        job_details['work_setting'] = driver.find_element(By.CSS_SELECTOR, "div.chip_chip__cYJs6 span[id^='location']").text
    except:
        job_details['work_setting'] = None

    # Scrape work mode (e.g., full-time, part-time)
    try:
        job_details['work_mode'] = driver.find_element(By.CSS_SELECTOR, "div.chip_chip__cYJs6 span[id^='employmentDetailChip']").text
    except:
        job_details['work_mode'] = None

    # Scrape job description and position ID
    try:
        read_full_description_button = driver.find_element(By.ID, "descriptionToggle")
        driver.execute_script("arguments[0].click();", read_full_description_button)
        time.sleep(1)
        job_description_html = driver.find_element(By.CSS_SELECTOR, "div[data-cy='jobDescription']").text
        job_details['job_description'] = job_description_html

        # Extract position ID from job description
        position_id_prefix = "Position Id: "
        position_id_start = job_description_html.find(position_id_prefix)
        if position_id_start != -1:
            position_id_start += len(position_id_prefix)
            position_id_end = job_description_html.find("\n", position_id_start)
            if position_id_end == -1:
                position_id_end = len(job_description_html)
            job_details['position_id'] = job_description_html[position_id_start:position_id_end].strip()
        else:
            job_details['position_id'] = None
    except:
        job_details['job_description'] = None
        job_details['position_id'] = None

    # Scrape company name
    try:
        job_details['company_name'] = driver.find_element(By.CSS_SELECTOR, "li.job-header_jobDetailFirst__xI_5S a[data-cy='companyNameLink']").text
    except:
        job_details['company_name'] = None

    # Scrape company URL
    try:
        job_details['company_url'] = driver.find_element(By.CSS_SELECTOR, "li.job-header_jobDetailFirst__xI_5S a[data-cy='companyNameLink']").get_attribute("href")
    except:
        job_details['company_url'] = None

    job_details['job_url'] = driver.current_url
    job_details['scraped_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return job_details
