#!/usr/bin/python3
from app.tools.courses_data import CoursesData
from config import FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR, PROGRAM, PKL_STORAGE_FILE

if __name__ == '__main__':
    print("initiating Course data by scraping using the config parameters...")
    courses_data = CoursesData(from_pkl=False, from_scrape=True,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR, program=PROGRAM)
    courses_data.save()
    print("Saved scraped courses")
