#!/usr/bin/python3

from config import REMOVABLE_CHARACTERS, AVAILABE_GRADES
from app.tools.courses_data import CoursesData
from app.tools.errors import handle_error
from app.tools.course import Course
from app.tools.student_course_summary import StudentCourseSummary

import sys, os
from subprocess import Popen
import tempfile
import re

UNFINISHED_COURSES_EN_HEADER = "Credits obtained in unfinished courses"
UNFINISHED_COURSES_SWE_HEADER = "Prov/moment i ej slutrapporterade kurser"
COURSES_EN_HEADER = "Courses"
COURSES_SWE_HEADER = "Avslutade kurser"

def get_student_results(pdf_file, courses_data):
    temp_pdf_text_file = tempfile.NamedTemporaryFile(delete=True)
    temp_pdf_text_file_name = pdf_to_text(pdf_file, temp_pdf_text_file.name)
    return parse_text(temp_pdf_text_file_name, courses_data.get_courses())

def pdf_to_text(pdf_file, temp_pdf_text_file_name):
    p = Popen(['pdftotext', pdf_file, temp_pdf_text_file_name])
    p.communicate()
    return temp_pdf_text_file_name

def parse_text(pdf_text_file, available_courses):
    grade_regex = re.compile(".*(\d+\.\d)_ ([{0}]).*".format(AVAILABE_GRADES))
    def grade_in_line(ling, grade_list):
        '''
        Checks if a line contains a grade, if so, the grade is added to
        the grade list.
        '''
        grade_match = grade_regex.match(line)
        if grade_match:
            points = float(grade_match.group(1))
            grade = grade_match.group(2)
            grade_list.append([grade, points])

    def course_in_line(line, course_list):
        '''
        Checks if a line contains a course code, if so, the course is added to
        the course list and True is returned.
        Otherwise, False is returned
        '''
        line = line.replace(REMOVABLE_CHARACTERS, '')
        words = line.split(' ')
        courses_in_line = [word for word in words if word in available_courses]
        if courses_in_line:
            course_list.append(available_courses[courses_in_line[0]])
            return True
        else:
            return False
    def determine_language(line):
        """Determines the language of the pdf, currently only supports swedish and english"""
        #TODO: remove hacky solution
        #Hacky way to check if it is swedish or english pdf
        if bool(re.search(r'\d',lines[1])):
            name = lines[3]
            course_header = COURSES_SWE_HEADER
            unfinished_courses_header = UNFINISHED_COURSES_SWE_HEADER
            version = "swe"
        else:
            name = lines[1]
            course_header = COURSES_EN_HEADER
            unfinished_courses_header = UNFINISHED_COURSES_EN_HEADER
            version = "eng"
        return name, course_header, unfinished_courses_header, version
    finished_courses = []
    unfinished_courses = []
    grade_list = []
    is_parsing_courses = False
    active_course_list = None
    version = "eng"
    with open(pdf_text_file, 'r') as pdf_text_file:
        lines = pdf_text_file.readlines()
        name, course_header, unfinished_courses_header, version = determine_language(lines[1])
        print(version)
        for line in lines:
            line = line.strip('\n')
            if line == course_header:
                is_parsing_courses = True
                active_course_list = finished_courses
            elif line == unfinished_courses_header:
                active_course_list = unfinished_courses
            elif is_parsing_courses:
                grade_in_line(line, grade_list)
                course_in_line(line, active_course_list)
    grade_list = grade_list[:len(finished_courses)]
    student_course_summary = StudentCourseSummary(version,name,finished_courses, unfinished_courses, grade_list)
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
