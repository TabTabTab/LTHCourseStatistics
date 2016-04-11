#!/usr/bin/python3

import sys
import os

from config import FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR, PROGRAM
from app.tools.course_database import CourseDatabase
from app.tools.pdf_reader import read_student_results, ReadPDFException
from app.tools.errors import handle_error


def get_course_statistics(pdf_file):
    from_pkl = True
    from_scrape = False
    course_database = CourseDatabase.factory(from_pkl=from_pkl, from_scrape=from_scrape,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR, program=PROGRAM)
    if from_scrape:
        #temporary testing line
        courses_data.save()
    try:
        student_results = read_student_results(pdf_file, course_database)
    except ReadPDFException as e:
        raise
    return student_results

def main(argv):
    if len(argv) < 1:
        handle_error("Please provide a course pdf file..")
    pdf_file = argv[0].strip()
    student_results = get_course_statistics(pdf_file)
    print(student_results)

if __name__ == '__main__':
    main(sys.argv[1:])
