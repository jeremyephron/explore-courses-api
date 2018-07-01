# Stanford Explore Courses Python API #

This package is a Python API for Stanford's Explore Courses site, which enables users to search through Stanford's catalog of over **13,000 courses**.

## Installation ##
Type the following command in terminal to install:

`pip install explorecourses`

## Usage ##
Import the package's classes into your Python program:

`from explorecourses import *`

Create a new CourseConnection:

`connect = CourseConnection()`

Query the Explore Courses database by department code:

`courses = connect.get_courses_by_department("MATH", year="2017-2018")`

Apply filters to your query:

`courses = connect.get_courses_by_query("all courses", filters.AUTUMN, filters.WAY_AII)`

## Sample Program ##
```python
from explorecourses import *
from explorecourses import filters

connect = CourseConnection()

# Print out all courses for 2017-2018.
year = "2017-2018"
for school in connect.get_schools(year):
    for dept in school.departments:
        courses = connect.get_courses_by_department(dept.code, year=year)
        for course in courses:
            print(course)

```


## Thanks ##
Thanks to Jim Sproch who wrote Stanford's Explore Courses Java API.
