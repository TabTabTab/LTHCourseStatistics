#!/usr/bin/python2

from config import REMOVABLE_CHARACTERS
from courses_data import CoursesData
from errors import handle_error
from course import Course
from student_course_summary import StudentCourseSummary

import sys, os
from subprocess import Popen
import tempfile

UNFINISHED_COURSES_HEADER = "Credits obtained in unfinished courses"
COURSES_HEADER = "Courses"

def get_student_results(pdf_file, courses_data):
    temp_pdf_text_file = tempfile.NamedTemporaryFile(delete=True)
    temp_pdf_text_file_name = pdf_to_text(pdf_file, temp_pdf_text_file.name)
    return parse_text(temp_pdf_text_file_name, courses_data.get_courses())

def pdf_to_text(pdf_file, temp_pdf_text_file_name):
    p = Popen(['pdftotext', pdf_file, temp_pdf_text_file_name])
    p.communicate()
    return temp_pdf_text_file_name

def parse_text(pdf_text_file, available_courses):
    def course_in_line(line, course_list):
        '''
        Checks if a line contains a course code, if so, the course is added to
        the course list.
        Otherwise, none is returned
        '''
        line = line.replace(REMOVABLE_CHARACTERS, '')
        words = line.split(' ')
        courses_in_line = [word for word in words if word in available_courses]
        if courses_in_line:
            course_list.append(available_courses[courses_in_line[0]])
        else:
            return None
    finished_courses = []
    unfinished_courses = []
    is_parsing_courses = False
    active_course_list = None
    with open(pdf_text_file, 'r') as pdf_text_file:
        for line in pdf_text_file:
            line = line.strip('\n')
            if line == COURSES_HEADER:
                is_parsing_courses = True
                active_course_list = finished_courses
            elif line == UNFINISHED_COURSES_HEADER:
                active_course_list = unfinished_courses
            elif is_parsing_courses:
                course_in_line(line, active_course_list)
    student_course_summary = StudentCourseSummary(finished_courses, unfinished_courses)
    return student_course_summary

def main(argv):
    if len(argv) < 1:
        handle_error("Please provide a course pdf file..")
    pdf_file = argv[0].strip()
    # just for test
    courses_data = CoursesData()
    courses_data.get_courses = lambda: {'EDAN40': Course(code='EDAN40', points=7.5, level='G2', initial_course_type="Test type")}

    read_course_data = get_student_results(pdf_file, courses_data)
    print(read_course_data)

if __name__ == '__main__':
    main(sys.argv[1:])
