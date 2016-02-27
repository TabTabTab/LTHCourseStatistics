#!/usr/bin/python2

from config import PKL_STORAGE_FILE, FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR,\
    COURSE_BASE_URL

from lxml import html
import requests
from collections import defaultdict
import time
import sys
import pickle

class StoredCourseData(object):
    '''
    Container for storing saved courses
    '''
    def __init__(self, courses_data=None, from_year=FROM_SCHOOL_YEAR,
        to_year=TO_SCHOOL_YEAR, last_update=time.time(), from_pkl=False):
        if from_pkl:
            self.load()
        else:
            self.courses_data = courses_data
            self.from_year = from_year
            self.to_year = to_year
            self.last_update = last_update

    def get_courses(self):
        return self.courses

    def save(self):
        with open(PKL_STORAGE_FILE, 'wb') as pkl_file:
            # Pickle dictionary using protocol 0.
            pickle.dump(self, pkl_file)

    def load(self):
        try:
            with open(PKL_STORAGE_FILE, 'rb') as pkl_file:
                stored_course_data = pickle.load(pkl_file)
                self.courses_data = stored_course_data.courses_data
                self.from_year = stored_course_data.from_year
                self.to_year = stored_course_data.to_year
                self.last_update = stored_course_data.last_update
                return self
        except IOError:
            handle_error("Could not access or find stored data in: '{0}'"
                .format(PKL_STORAGE_FILE))
    def __str__(self):
        return """from year: {0}, to year: {1}, last update {2}, course_data:\
            \n{3}""".format(
            self.from_year, self.to_year, self.last_update, self.courses_data)

class Course(object):
    '''
    Represents a course
    '''
    def __init__(self, code, points, level, initial_course_type=None):
        self.course_code = code
        self.points = points
        self.level = level
        self.course_types = [initial_course_type] if initial_course_type else []

    def __str__(self):
        return "course code: {0}, points: {1}, level {2}, types: {3}".format(
            self.course_code, self.points, self.level, self.course_types)

    def __repr__(self):
        return "{0}\n".format(self.__str__())

    def get_course_code(self):
        return self.course_code

    def merge_course_info(self, other_course):
        '''
        Merges the information from the other course too the current course
        This currently only concerns the course types
        '''
        self.course_types += other_course.course_types

def handle_error(error_msg="An error occured", exit=True):
    print(error_msg)
    if exit:
        sys.exit(1)

def get_school_years(from_year, to_year):
    '''
    Creates a list of school years in string format
    from_year (int) - the year the first school year starts
    to_year (int) - the year the last school year ends
    '''
    return ["{0}_{1}".format(year, year + 1)
        for year in xrange(from_year, to_year)]

def course_table_info(course_table, school_year, container):
    '''
    Scrapes information about courses in a html table elements
    by traversing it.
    The courses are then added to the container
    '''
    table_parent = course_table.getparent()
    th3_above_parent = table_parent.getprevious()
    course_type = th3_above_parent.text
    course_body = course_table.getchildren()[1] #this should give us the "tbody"
    courses = course_body.getchildren()

    for course_html in courses:
        course = html_to_course(course_html, course_type)
        add_course(course, container)

def add_course(course, container):
    '''
    Adds a course to a container. If the course already exists in the
    container, the courses are merged
    '''
    if course is not None:
        course_code = course.get_course_code()
        if course_code in container:
            container[course_code].merge_course_info(course)
        else:
            container[course_code] = course

def html_to_course(course_element, course_type):
    '''
    Scrapes information from a html course element and creates a course object
    containing the gathered information
    '''
    course = None
    try:
        vals = ["points", "level"]
        elements = course_element.getchildren()
        course_code = elements[0].getchildren()[0].text
        info = dict(zip(vals, map(lambda e:e.text, elements[1:])))
        points = float(info['points'].replace(',','.'))
        level = info['level']
        course = Course(course_code, points, level, course_type)
    except IndexError:
        return None
    return course

def update_courses_data():
    '''
    Scrapes the LTH course pages in order to replace
    the current stored courses data
    '''
    courses_data = dict()
    school_years = get_school_years(FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR)
    for school_year in school_years:
        print ("Updating ", school_year)
        url = COURSE_BASE_URL.format(school_year)
        try:
            page = requests.get(url)
            page.encoding = 'utf-8'
            html_tree = html.fromstring(page.text)
            course_tables = html_tree.xpath('//table[@class="CourseListView border hover zebra"]')
            for course_table in course_tables:
                course_table_info(course_table, school_year, courses_data)
        except requests.exceptions.ConnectionError:
            handle_error("Failed to establish connection")
    StoredCourseData(courses_data).save()


if __name__ == '__main__':
    update_courses_data()
    print(StoredCourseData(from_pkl=True))
