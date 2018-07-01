from xml.etree import ElementTree as ET

from explorecourses import *

class TestSchedule(object):

    @classmethod
    def setup_class(cls):
        text_sched = (
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
        )

        cls.xml_sched = ET.fromstring(text_sched)


    def test_create_schedule(self):
        sched = Schedule(self.xml_sched)

        assert sched != None


    def test_schedule_attrs(self):
        sched = Schedule(self.xml_sched)

        assert sched.start_date == "Sep 25, 2017"
        assert sched.end_date == "Dec 8, 2017"
        assert sched.start_time == "11:30:00 AM"
        assert sched.end_time == "12:20:00 PM"
        assert sched.location == "320-105"
        assert sched.days == ("Monday", "Wednesday", "Friday")
        assert len(sched.instructors) == 2 


    def test_schedule_string(self):
        sched = Schedule(self.xml_sched)

        assert str(sched) == ("Monday, Wednesday, Friday, 11:30:00 AM - "
                              "12:20:00 PM at 320-105")
