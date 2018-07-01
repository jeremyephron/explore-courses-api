"""
This module contains classes representing various academic elements 
for use in storing and manipulating information from Explore Courses.

Includes:
    - School
    - Department
    - Course
    - Section
    - Schedule
    - Instructor
    - LearningObjective
    - Attribute
    - Tag
"""

from typing import Tuple
from xml.etree.ElementTree import Element


class Department(object):
    """
    This class represents a department within a school.

    Attributes:
        name (str): The department name.
        code (str): The department code used for searching courses by 
            department.
    """

    def __init__(self, elem: Element):
        """
        Constructs a new Department from an XML element.

        Args:
            elem (Element): The department's XML element.

        """

        self.name = elem.get("longname")
        self.code = elem.get("name")


    def __str__(self):
        """
        Returns a string representation of the Department that includes both 
        department name and code.

        """

        return f"{self.name} ({self.code})"


class School(object):
    """
    This class represents a school within the university.

    Attributes:
        name (str): The name of the school.
        departments (Tuple[Department]): A list of departments within the 
            school.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new School from an XML element.

        Args:
            elem (Element): The school's XML element.

        """

        self.name = elem.get("name")

        depts = elem.findall("department")
        self.departments = tuple(Department(dept) for dept in depts)


    def get_department(self, idf: str) -> Department:
        """
        Gets a department within the school identified by name or code.

        Args:
            idf (str): An identifier of the department; either the name or code.

        Returns:
            Department: The department matched by the given identifier if a 
                match was found, None otherwise.
        
        """

        idf = idf.lower()

        find_code = lambda dept, code: dept.code.lower() == code
        find_name = lambda dept, name: dept.name.lower() == name
        find_dept = lambda dept, idf: find_name(dept, idf) or find_code(dept, 
                                                                        idf)

        idx = [idx for idx, dept in enumerate(self.departments)
               if find_dept(dept, idf)]

        return self.departments[idx[0]] if idx else None


    def __str__(self):
        """
        Returns a string representation of the School that is the School's name.

        """

        return self.name


class Instructor(object):
    """
    This class represents an instructor for a section.

    Attributes:
        name (str): The instructor's name in "LastName, FirstInitial." form.
        first_name (str): The instructor's first name.
        middle_name (str): The instructor's middle name.
        last_name (str): The instructor's last name.
        sunet_id (str): The instructor's SUNet ID (as in sunet_id@stanford.edu).
        is_primary_instructor (bool): True if the instructor is the primary 
            instructor for the course, False otherwise.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new Instructor from an XML element.

        Args:
            elem (Element): The instructor's XML element.

        """

        self.name = elem.findtext("name")
        self.first_name = elem.findtext("firstName")
        self.middle_name = elem.findtext("middleName")
        self.last_name = elem.findtext("lastName")
        self.sunet_id = elem.findtext("sunet")
        self.is_primary_instructor = elem.findtext("role") == "PI"


    def __str__(self):
        """
        Returns a string representation of the Instructor that includes the 
        instructor's first and last name and SUNet ID.

        """

        return f"{self.first_name} {self.last_name} ({self.sunet_id})"


class Attribute(object):
    """
    This class represents an attribute of a course.

    Attributes:
        name (str): The name of the attribute.
        value (str): The abbreviation value of the attribute.
        description (str): A description of the value of the attribute.
        catalog_print (bool): True if the attribute has the catalog print flag, 
            False otherwise.
        schedule_print (bool): True if the attribute has the schedule print 
            flag, False otherwise.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new Attribute from an XML element.

        Args:
            elem (Element): The attribute's XML element.

        """

        self.name = elem.findtext("name")
        self.value = elem.findtext("value")
        self.description = elem.findtext("description")
        self.catalog_print = elem.findtext("catalogPrint") == "true"
        self.schedule_print = elem.findtext("schedulePrint") == "true"


    def __str__(self):
        """
        Returns a string representation of the Attribute that includes the 
        attribute's name and value.

        """

        return f"{self.name}::{self.value}"


class Schedule(object):
    """
    This class represents the schedule of a section, including instructors.

    Attributes:
        start_date (str): The start date of the section's schedule.
        end_date (str): The end date of the section's schedule.
        start_time (str): The start time of each section.
        end_time (str): The end time of each section.
        location (str): The location of each section.
        days (Tuple[str]): The days of the week that the section meets.
        instructors (Tuple[Instructor]): The section's instructors.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new Schedule from an XML element.

        Args:
            elem (Element): The schedule's XML element.

        """

        self.start_date = elem.findtext("startDate")
        self.end_date = elem.findtext("endDate")
        self.start_time = elem.findtext("startTime")
        self.end_time = elem.findtext("endTime")
        self.location = elem.findtext("location")
        self.days = tuple(elem.findtext("days").split())
        self.instructors = tuple(Instructor(instr) for instr 
                                 in elem.find("instructors"))


    def __str__(self):
        """
        Returns a string representation of the Schedule that includes the 
        days of the week the section meets and it's time and location.

        """

        return (f"{', '.join(self.days)}, {self.start_time} - {self.end_time} "
                f"at {self.location}")


class Section(object):
    """
    This class represents a section of a course.

    Attributes:
        class_id (int): The unique ID of the section.
        term (str): The year and quarter during which the section is offered.
        units (str): The number of units the section is offered for
        section_num (str): The section number which distinguishes between 
            different sections of the same type.
        component (str): The type of section (e.g., LEC)
        curr_class_size (int): The current number of students enrolled in the 
            section.
        max_class_size (int): The maximum number of students allowed in the 
            section.
        curr_waitlist_size (int): The current number of students on the 
            waitlist to enroll in the section.
        max_waitlist_size (int): The maximum number of students allowed on the 
            waitlist for the section.
        notes (str): Any notes about the section.
        schedules (Tuple[Schedule]): The different schedules of the section.
        attributes (Tuple[Attribute]): The section's attributes.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new Section from an XML element.

        Args:
            elem (Element): The section's XML element.

        """

        self.class_id = int(elem.findtext("classId"))
        self.term = elem.findtext("term")
        self.units = elem.findtext("units")
        self.section_num = elem.findtext("sectionNumber")
        self.component = elem.findtext("component")
        self.max_class_size = int(elem.findtext("maxClassSize"))
        self.curr_class_size = int(elem.findtext("currentClassSize"))
        self.curr_waitlist_size = int(elem.findtext("currentWaitlistSize"))
        self.max_waitlist_size = int(elem.findtext("maxWaitlistSize"))
        self.notes = elem.findtext("notes")

        self.schedules = tuple(Schedule(sched) for sched 
                               in elem.find("schedules"))

        self.attributes = tuple(Attribute(attr) for attr 
                                in elem.find("attributes"))


    def __str__(self):
        """
        Returns a string representation of the Section that includes the 
        section's component and number, and section's ID.

        """

        return f"{self.component} {self.section_num} (id: {self.class_id})"


class Tag(object):
    """
    This class represents a tag for a course.

    Attributes:
        organization (str): The organization within the school responsible for 
            the tag.
        name (str): The name of the tag.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new Tag from an XML element.

        Args:
            elem (Element): The tag's XML element.

        """

        self.organization = elem.findtext("organization")
        self.name = elem.findtext("name")


    def __str__(self):
        """
        Returns a string representation of the Tag that includes the 
        tag's organization and name.

        """

        return f"{self.organization}::{self.name}"


class LearningObjective(object):
    """
    This class represents a learning objective for a course.

    Attributes:
        code (str): The GER that the learning objective is for.
        description (str): A description of the learning objective.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new LearningObjective from an XML element.

        Args:
            elem (Element): The learning objective's XML element.

        """

        self.code = elem.findtext(".//requirementCode")
        self.description = elem.findtext(".//description")


    def __str__(self):
        """
        Returns a string representation of the LearningObjective that includes 
        the learning objective's code and description.

        """

        return f"Learning Objective ({self.code}: {self.description})"


class Course(object):
    """
    This class represents a course listed at the university.

    Attributes:
        year (str): The Academic year that the course is offered.
        subject (str): The academic subject of the course (e.g., 'MATH').
        code (str): The code listing of the course (e.g., '51').
        title (str): The full title of the course.
        description (str): A description of the course.
        gers (Tuple[str]): The General Education Requirements satisfied 
            by the course.
        repeatable (bool): True if the course is repeatable for credit, 
            False otherwise.
        grading_basis (str): The grading basis options for the course.
        units_min (int): The minimum number of units the course can be 
            taken for.
        units_max (int): The maximum number of units the course can be 
            taken for.
        objectives (Tuple[LearningObjective]): The learning objectives of 
            the course.
        final_exam (bool): True if the course has a final exam, False otherwise.
        sections (Tuple[Section]): The sections associated with the course.
        tags (Tuple[Tag]): The tags associated with the course.
        attributes (Tuple[Attributes]): The attributes associated with 
            the course.
        course_id (int): The unique ID of the course.
        active (bool): True if the course is currently being taught, 
            False otherwise.
        offer_num (str): The offer number of the course.
        academic_group (str): The academic group that the course is a part of.
        academic_org (str): The academic organization that the course 
            is a part of.
        academic_career (str): The academic career associated with the course.
        max_units_repeat (int): The number of units that the course 
            can be repeated for.
        max_times_repeat (int): The number of times that the course 
            can be repeated.

    """

    def __init__(self, elem: Element):
        """
        Constructs a new Course from an XML element.

        Args:
            elem (Element): The course's XML element.

        """

        self.year = elem.findtext("year")
        self.subject = elem.findtext("subject")
        self.code = elem.findtext("code")
        self.title = elem.findtext("title")
        self.description = elem.findtext("description")
        self.gers = tuple(elem.findtext("gers").split(", "))
        self.repeatable = (True if elem.findtext("repeatable") == "true" 
                           else False)

        self.grading_basis = elem.findtext("grading")
        self.units_min = int(elem.findtext("unitsMin"))
        self.units_max = int(elem.findtext("unitsMax"))
        self.objectives = tuple(LearningObjective(obj) for obj 
                                in elem.find("learningObjectives"))

        self.final_exam = (
            True if elem.findtext(".//finalExamFlag") == "Y" 
            else False if elem.findtext(".//finalExamFlag") == "N" 
            else None
        )

        self.sections = tuple(Section(section) for section 
                              in elem.find("sections"))

        self.tags = tuple(Tag(tag) for tag in elem.find("tags"))
        self.attributes = tuple(Attribute(attr) for attr 
                                in elem.find("attributes"))

        self.course_id = int(elem.findtext(".//courseId"))

        self.active = (True if elem.findtext(".//effectiveStatus") == "A" 
                       else False if elem.findtext(".//effectiveStatus") == "I" 
                       else None)

        self.offer_num = elem.findtext(".//offerNumber")
        self.academic_group = elem.findtext(".//academicGroup")
        self.academic_org = elem.findtext(".//academicOrganization")
        self.academic_career = elem.findtext(".//academicCareer")
        self.max_units_repeat = int(elem.findtext(".//maxUnitsRepeat"))
        self.max_times_repeat = int(elem.findtext(".//maxTimesRepeat"))


    def __str__(self):
        """
        Returns a string representation of the Course that includes the 
        course's subject, code, and full title.

        """

        return f"{self.subject}{self.code} {self.title}"


    def __eq__(self, other):
        """
        Overloads the equality (==) operator for the Course class.
        
        A Course can only be compared to another Course. Course equality is 
        determined by course ID.

        Args:
            other: The right operand of the equality operator.

        Returns:
            bool: True if the object being compared is equal to the Course, 
                False otherwise.

        """

        if type(other) != Course: return False
        return self.course_id == other.course_id


    def __lt__(self, other):
        """
        Overloads the less than (<) operator for Course.

        A Course can only be compared to another Course. Courses are compared 
        first by subject, then by code, and last by year.

        Args:
            other: The right operand of the less than operator.

        Returns:
            bool: True if the object being compared is less than the Course, 
                False otherwise.
        """

        if type(other) != Course: return False
        if self.subject != other.subject:
            return self.subject < other.subject
        if self.code != other.code:
            return self.code < other.code
        if self.year != other.year:
            return self.year < other.year
        return False


    def __gt__(self, other):
        """
        Overloads the greater than (>) operator for Course.

        A Course can only be compared to another Course. Courses are compared 
        first by subject, then by code, and last by year.

        Args:
            other: The right operand of the greater than operator.

        Returns:
            bool: True if the object being compared is greater than the Course, 
                False otherwise.
        """

        if type(other) != Course: return False
        if self.subject != other.subject:
            return self.subject > other.subject
        if self.code != other.code:
            return self.code > other.code
        if self.year != other.year:
            return self.year > other.year
        return False


    def __le__(self, other):
        """
        Overloads the less than or equal to operator (<=) for Course.

        A Course can only be compared to another Course. Courses are compared 
        first by subject, then by code, and last by year.

        Args:
            other: The right operand of the less than or equal to operator.

        Returns:
            bool: True if the object being compared is less than or equal to 
            the Course, False otherwise.

        """

        return self.__lt__(other) or self.__eq__(other)


    def __ge__(self, other):
        """
        Overloads the greater than or equal to operator (>=) for Course.

        A Course can only be compared to another Course. Courses are compared 
        first by subject, then by code, and last by year.

        Args:
            other: The right operand of the greater than or equal to operator.

        Returns:
            bool: True if the object being compared is greater than or equal to 
            the Course, False otherwise.

        """

        return self.__gt__(other) or self.__eq__(other)
