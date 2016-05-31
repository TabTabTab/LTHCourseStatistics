# LTHCourseStatistics


## Set Up

### Initial Preparations
1. clone the repository to your chosen location
  $ git clone https://github.com/TabTabTab/LTHCourseStatistics.git
2. make sure you have python3.4 is installed
  $ sudo apt-get install python3.4
3. make sure pip3 is installed
  $ sudo apt-get install python3-pip
4. install flask for python3
  $ sudo pip3 install flask
5. install lxml for python3
  $ sudo pip3 install lxml

### Scraping for courses
You need to scrape for courses before you can start the web service.
    $ cd services
    You may now edit the config file to set up your specific scraper settings.
    Then you can run the initiation script which will scrape for courses, this may take up to a minute.
    $ ./initiate.py


## Run the service
Execute the run program
  $ cd services
  $ ./run.py

### Debug mode
You may run the service in debug mode, either by specifying this in the
service/config.py file or by supplying the 'debug' argument to run.py
  $ ./run.py debug


## Errors and fixes
1. ImportError: No module named 'lxml'
    $ pip3 install --upgrade lxml
