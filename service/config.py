import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PKL_STORAGE_FILE = os.path.join(BASE_DIR, 'app', 'pkl', 'courses_data.pkl')

FROM_SCHOOL_YEAR = 10
TO_SCHOOL_YEAR = 16

PROGRAM = 'D'

AVAILABE_GRADES = "345G"

#the grades that should be used for average grade calculations and their weight
WEIGHTED_GRADES = { '3':3,
                    '4':4,
                    '5':5}

COURSE_BASE_URL = "http://kurser.lth.se/lot/?lasar={0}&sort1=lp&sort2=slut_lp&sort3=namn&prog={1}&forenk=t&val=program&lang=en"



TEMO_FILE_BASENAME = os.path.join(BASE_DIR, "temp", "temp_pdf")

#do not write space here
REMOVABLE_CHARACTERS = '-'
