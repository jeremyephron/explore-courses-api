from xml.etree import ElementTree as ET

from explorecourses import *

class TestSchool(object):

    @classmethod
    def setup_class(cls):
        text_elem = (
            '<school name="Graduate School of Business">'
            '<department longname="Accounting" name="ACCT"/>'
            '<department longname="Economic Analysis and Policy" '
            'name="MGTECON"/>'
            '<department longname="Finance" name="FINANCE"/>'
            '<department longname="Human Resource Management" name="HRMGT"/>'
            '<department longname="Marketing" name="MKTG"/>'
            '<department longname="Organizational Behavior" name="OB"/>'
            '<department longname="Political Economics" name="POLECON"/>'
            '<department longname="Strategic Management" name="STRAMGT"/>'
            '</school>'
        )

        cls.xml_elem = ET.fromstring(text_elem)


    def test_create_school(self):
        school = School(self.xml_elem)

        assert school != None


    def test_school_methods(self):
        name = "Graduate School of Business"
        dept_name = "Political Economics"
        dept_code = "POLECON"
        n_depts = 8

        school = School(self.xml_elem)

        assert school.name == name
        assert len(school.departments) == n_depts
        assert (school.get_department(dept_name) 
                == school.get_department(dept_code))
