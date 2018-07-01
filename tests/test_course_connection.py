from explorecourses import *
from explorecourses import filters

class TestCourseConnection(object):

    @classmethod
    def setup_class(cls):
        cls.connection = CourseConnection()


    def test_get_schools(self):
        schools = self.connection.get_schools()

        assert schools != None
        assert all([isinstance(sch, School) for sch in schools]) == True


    def test_get_school(self):
        school = self.connection.get_school("School of Engineering")

        assert school != None
        assert type(school) == School


    def test_get_courses_by_department(self):
        courses = self.connection.get_courses_by_department("POLECON")

        assert len(courses) > 0
        assert courses[0].subject == "POLECON"


    def test_get_courses_by_department_with_filters(self):
        courses = self.connection.get_courses_by_department("POLECON", 
                                                            filters.AUTUMN)

        assert len(courses) > 0
        assert (any("Autumn" in sect.term for sect in courses[0].sections) 
                == True)

        courses = self.connection.get_courses_by_department("MATH", 
                                                            filters.WAY_FR)

        assert len(courses) > 0
        assert ("WAY-FR" in courses[0].gers) == True
