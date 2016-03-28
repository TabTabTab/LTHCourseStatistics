import os

# Debug mode info

## shoudl the debug mode be active
IS_DEBUG = True


# Paths

## Base directory for the service (may also be refered to as a root directory)
SERVICE_BASE_DIR = os.path.dirname(os.path.realpath(__file__))

## The folder where the uploaded PDFs should be placed in
UPLOAD_FOLDER = os.path.join(SERVICE_BASE_DIR, 'app', 'tmp')

## The location of the "course database"
PKL_STORAGE_FILE = os.path.join(SERVICE_BASE_DIR, 'app', 'pkl', 'courses_data.pkl')

# Scraper Settings
COURSE_BASE_URL = "http://kurser.lth.se/lot/?lasar={0}&sort1=lp&sort2=slut_lp&sort3=namn&prog={1}&forenk=t&val=program&lang=en"

## The first year that should be scraped for courses
FROM_SCHOOL_YEAR = 10

## The first year that should be scraped for courses
TO_SCHOOL_YEAR = 16

## The programme to scrape for
PROGRAM = 'D'

## The different grades that will be scraped for
AVAILABE_GRADES = "345G"

## The grades that should be used for average grade calculations and their weight
WEIGHTED_GRADES = { '3':3,
                    '4':4,
                    '5':5}


# Other settings

## Allowed file endings of uploaded files
ALLOWED_EXTENSIONS = set(['pdf'])

## Characters that will be removed when checking for courses in a PDF (do not write space here)
COURSE_LINE_REMOVABLE_CHARACTERS = '-'
