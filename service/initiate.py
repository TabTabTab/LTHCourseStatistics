#!/usr/bin/python3
from app.tools.course_database import CourseDatabase
from config import FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR, PROGRAM, PKL_STORAGE_FILE

if __name__ == '__main__':
    print("initiating Course data by scraping using the config parameters...")
    course_database = CourseDatabase.factory(from_pkl=False, from_scrape=True,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR, program=PROGRAM)
    course_database.save()
    print("Saved scraped courses")
    print("Data saved in \"{0}\"".format(PKL_STORAGE_FILE))
