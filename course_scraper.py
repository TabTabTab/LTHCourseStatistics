#!/usr/bin/python2

from config import COURSE_BASE_URL
from course import Course
from errors import handle_error

from lxml import html
import requests

def list_school_years(from_year, to_year):
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

def scrape_courses_data(from_year, to_year, program):
    '''
    Scrapes the LTH course pages in order to replace
    the current stored courses data
    '''
    courses_data = dict()
    school_years = list_school_years(from_year, to_year)
    for school_year in school_years:
        print ("Updating ", school_year, program)
        url = COURSE_BASE_URL.format(school_year, program)
        try:
            page = requests.get(url)
            page.encoding = 'utf-8'
            html_tree = html.fromstring(page.text)
            course_tables = html_tree.xpath('//table[@class="CourseListView border hover zebra"]')
            for course_table in course_tables:
                course_table_info(course_table, school_year, courses_data)
        except requests.exceptions.ConnectionError:
            handle_error("Failed to establish connection")
    return courses_data

if __name__ == '__main__':
    print(scrape_courses_data(10, 11, 'D'))
