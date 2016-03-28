#!/usr/bin/python3

from config import IS_DEBUG

import sys

def main(argv):
    from app import app
    app.debug = "debug" in argv or IS_DEBUG
    app.run(port=5006)

if __name__ == '__main__':
    main(sys.argv)
