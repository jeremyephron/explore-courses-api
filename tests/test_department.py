from xml.etree import ElementTree as ET

from explorecourses import Department

class TestDepartment(object):

    def setup_class(cls):
        text_elem = ('<department longname="Political Economics" '
                     'name="POLECON"/>')

        cls.xml_elem = ET.fromstring(text_elem)


    def test_create_dept(self):
        dept = Department(self.xml_elem)

        assert dept != None


    def test_school_methods(self):
        name = "Political Economics"
        code = "POLECON"

        dept = Department(self.xml_elem)

        assert dept.name == name
        assert dept.code == code
