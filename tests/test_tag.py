from xml.etree import ElementTree as ET

from explorecourses import *

class TestTag(object):

    @classmethod
    def setup_class(cls):
        text_tag = (
            '<tag>'
            '<organization>EARTHSYS</organization>'
            '<name>energy_foundation</name>'
            '</tag>'
        )

        cls.xml_tag = ET.fromstring(text_tag)


    def test_create_tag(self):
        tag = Tag(self.xml_tag)

        assert tag != None


    def test_tag_attributes(self):
        tag = Tag(self.xml_tag)

        assert tag.organization == "EARTHSYS"
        assert tag.name == "energy_foundation"


    def test_tag_string(self):
        tag = Tag(self.xml_tag)
        assert str(tag) == "EARTHSYS::energy_foundation"
