#!/usr/bin/python3

import sys

from config import FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR, PROGRAM
from courses_data import CoursesData
from pdf_parser import get_student_results
from errors import handle_error


def course_statistics(pdf_file):
    courses_data = CoursesData(from_pkl=True, from_scrape=False,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR, program=PROGRAM)
    student_results = get_student_results(pdf_file, courses_data)
    return student_results
    #print(read_course_data)

def main(argv):
    if len(argv) < 1:
        handle_error("Please provide a course pdf file..")
    pdf_file = argv[0].strip()
    # just for test
    courses_data = CoursesData(from_pkl=True, from_scrape=False,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR, program=PROGRAM)
    #courses_data.save()
    student_results = get_student_results(pdf_file, courses_data)
    print(student_results)

if __name__ == '__main__':
    main(sys.argv[1:])
