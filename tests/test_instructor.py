from xml.etree import ElementTree as ET

from explorecourses import *

class TestInstructor(object):

    @classmethod
    def setup_class(cls):
        text_instructor = (
            '<instructor>'
            '<name>Wilson, J.</name>'
            '<firstName>Jenny</firstName>'
            '<middleName>Catherine</middleName>'
            '<lastName>Wilson</lastName>'
            '<sunet>jchw</sunet>'
            '<role>PI</role>'
            '</instructor>'
        )

        cls.xml_instr = ET.fromstring(text_instructor)


    def test_create_instructor(self):
        instr = Instructor(self.xml_instr)

        assert instr != None


    def test_instr_attributes(self):
        instr = Instructor(self.xml_instr)

        assert instr.name == "Wilson, J."
        assert instr.first_name == "Jenny"
        assert instr.middle_name == "Catherine"
        assert instr.last_name == "Wilson"
        assert instr.sunet_id == "jchw"
        assert instr.is_primary_instructor == True


    def test_instr_string(self):
        instr = Instructor(self.xml_instr)

        assert str(instr) == "Jenny Wilson (jchw)"
