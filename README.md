# LTHCourseStatistics


## Set Up
1. clone the repository to your chosen location
  $ git clone https://github.com/TabTabTab/LTHCourseStatistics.git
2. make sure you have python3.4 is installed
  $ sudo apt-get install python3.4
3. make sure pip3 is installed
  $ sudo apt-get install python3-pip
4. install flask for python3
  $ sudo pip3 install flask

## Error
1. ImportError: No module named 'lxml'.
   $ pip3 install --upgrade lxml


### Scraping for courses
You need to scrape for courses before you can start the web service.
    $ cd services
    $ ./initiate.py

## Run the service
Execute the run program
  $ cd services
  $ ./run.py
