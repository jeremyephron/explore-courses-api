from xml.etree import ElementTree as ET

from explorecourses import *

class TestSchedule(object):

    @classmethod
    def setup_class(cls):
        text_sect = (
            '<section>'
            '<classId>16518</classId>'
            '<term>2017-2018 Autumn</term>'
            '<termId>1182</termId>'
            '<subject>MATH</subject>'
            '<code>20</code>'
            '<units>3</units>'
            '<sectionNumber>02</sectionNumber>'
            '<component>LEC</component>'
            '<numEnrolled>51</numEnrolled>'
            '<maxEnrolled>50</maxEnrolled>'
            '<numWaitlist>0</numWaitlist>'
            '<maxWaitlist>0</maxWaitlist>'
            '<enrollStatus>Closed</enrollStatus>'
            '<addConsent>N</addConsent>'
            '<dropConsent>N</dropConsent>'
            '<courseId>117229</courseId>'
            '<schedules>'
            '<schedule>'
            '<startDate>Sep 25, 2017</startDate>'
            '<endDate>Dec 8, 2017</endDate>'
            '<startTime>11:30:00 AM</startTime>'
            '<endTime>12:20:00 PM</endTime>'
            '<location>320-105</location>'
            '<days>'
            'Monday Wednesday Friday'
            '</days>'
            '<instructors>'
            '<instructor>'
            '<name>Wilson, J.</name>'
            '<firstName>Jenny</firstName>'
            '<middleName>Catherine</middleName>'
            '<lastName>Wilson</lastName>'
            '<sunet>jchw</sunet>'
            '<role>PI</role>'
            '</instructor>'
            '<instructor>'
            '<name>Cant, D.</name>'
            '<firstName>Dylan</firstName>'
            '<middleName>Jesse</middleName>'
            '<lastName>Cant</lastName>'
            '<sunet>dcant</sunet>'
            '<role>TA</role>'
            '</instructor>'
            '</instructors>'
            '</schedule>'
            '</schedules>'
            '<currentClassSize>51</currentClassSize>'
            '<maxClassSize>50</maxClassSize>'
            '<currentWaitlistSize>0</currentWaitlistSize>'
            '<maxWaitlistSize>0</maxWaitlistSize>'
            '<notes/>'
            '<attributes>'
            '<attribute>'
            '<name>NQTR</name>'
            '<value>SPR</value>'
            '<description>Spring</description>'
            '<catalogPrint>true</catalogPrint>'
            '<schedulePrint>false</schedulePrint>'
            '</attribute>'
            '<attribute>'
            '<name>NQTR</name>'
            '<value>WIN</value>'
            '<description>Winter</description>'
            '<catalogPrint>true</catalogPrint>'
            '<schedulePrint>false</schedulePrint>'
            '</attribute>'
            '<attribute>'
            '<name>NQTR</name>'
            '<value>AUT</value>'
            '<description>Autumn</description>'
            '<catalogPrint>true</catalogPrint>'
            '<schedulePrint>false</schedulePrint>'
            '</attribute>'
            '</attributes>'
            '</section>'
        )

        cls.xml_sect = ET.fromstring(text_sect)


    def test_create_section(self):
        sect = Section(self.xml_sect)

        assert sect != None


    def test_section_attrs(self):
        sect = Section(self.xml_sect)

        assert sect.class_id == 16518
        assert sect.term == "2017-2018 Autumn"
        assert sect.units == "3"
        assert sect.section_num == "02"
        assert sect.component == "LEC"
        assert sect.max_class_size == 50
        assert sect.curr_class_size == 51
        assert sect.curr_waitlist_size == 0
        assert sect.max_waitlist_size == 0
        assert sect.notes == ""
        assert len(sect.schedules) == 1
        assert len(sect.attributes) == 3


    def test_section_string(self):
        sect = Section(self.xml_sect)

        assert str(sect) == "LEC 02 (id: 16518)"

