from xml.etree import ElementTree as ET

from explorecourses import *

class TestAttribute(object):

    @classmethod
    def setup_class(cls):
        text_attr = (
            '<attribute>'
            '<name>NQTR</name>'
            '<value>SPR</value>'
            '<description>Spring</description>'
            '<catalogPrint>true</catalogPrint>'
            '<schedulePrint>false</schedulePrint>'
            '</attribute>'
        )

        cls.xml_attr = ET.fromstring(text_attr)


    def test_create_attribute(self):
        self.attr = Attribute(self.xml_attr)

        assert self.attr != None


    def test_attribute_attrs(self):
        self.attr = Attribute(self.xml_attr)

        assert self.attr.name == "NQTR"
        assert self.attr.value == "SPR"
        assert self.attr.description == "Spring"
        assert self.attr.catalog_print == True
        assert self.attr.schedule_print == False
