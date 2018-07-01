"""
This module implements the CourseConnection class, which is the main entrypoint 
for the Explore Courses API.
"""

import requests
from typing import List, Tuple
import xml.etree.ElementTree as ET

from explorecourses.classes import School, Course

class CourseConnection():
    """
    This class is the main entrypoint for the Explore Courses API, which 
    establishes the HTTP connection and makes all requests.
    """

    _URL = "http://explorecourses.stanford.edu/"

    def __init__(self):
        """ 
        Constructs a new CourseConnection by beginning a requests session.

        """

        self._session = requests.Session()


    def get_schools(self, academic_year=None) -> List[School]:
        """
        Gets all schools within the university.

        Args:
            academic_year (Optional[str]): The academic year within which to 
                retrive schools from (e.g., "2017-2018"). Defaults to None.

        Returns:
            List[School]: The schools contained within the university.

        """

        payload = {"view": "xml-20120105", "year": academic_year}
        res = self._session.get(self._URL, params=payload)

        root = ET.fromstring(res.content)
        schools = root.findall(".//school")

        return [School(school) for school in schools]


    def get_school(self, name: str) -> School:
        """
        Gets a school within the university by name.

        Args:
            name (str): The name of the school.the

        Returns:
            School: The school if it exists, None otherwise.

        """

        schools = self.get_schools()
        f = lambda school, name: school.name == name

        idx = [idx for idx, school in enumerate(schools) if f(school, name)]

        return schools[idx[0]] if idx else None


    def get_courses_by_department(self, code: str, *filters: str, 
                                  year=None) -> List[Course]:

        """
        Gets all courses listed under a given department.

        Args:
            code (str): The department code.
            *filters (str): Search query filters.
            year (Optional[str]): The academic year within which to retrieve 
                courses (e.g., "2017-2018"). Defaults to None.

        Returns:
            List[Course]: The courses listed under the given department.

        """

        filters = list(filters)
        filters.append(f"filter-departmentcode-{code}")

        return self.get_courses_by_query(code, *filters, year=year)


    def get_courses_by_query(self, query: str, *filters: str, 
                             year=None) -> List[Course]:

        """
        Gets all courses matched by a search query.

        Args:
            query (str): The search query.
            *filters (str): Search query filters.
            year (Optional[str]): The academic year within which to retrieve 
                courses (e.g., "2017-2018"). Defaults to None.

        Returns:
            List[Course]: The courses matching the search query.

        """

        url = self._URL + "search"

        payload = {
            "view": "xml-20140630",
            "filter-coursestatus-Active": "on",
            "q": query,
        }
        payload.update({f: "on" for f in filters})
        if year: payload.update({"academicYear": year})

        res = self._session.get(url, params=payload)

        root = ET.fromstring(res.content)
        courses = root.findall(".//course")

        return [Course(course) for course in courses]
