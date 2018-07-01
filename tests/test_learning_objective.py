from xml.etree import ElementTree as ET

from explorecourses import *

class TestSchedule(object):

    @classmethod
    def setup_class(cls):
        text_obj = (
            '<learningObjective>'
            '<requirementCode>WAY-FR</requirementCode>'
            '<description>'
            'solve equations or optimization problems through translation '
            'to a standardized formalism.'
            '</description>'
            '</learningObjective>'
        )

        cls.xml_obj = ET.fromstring(text_obj)


    def test_create_learning_objective(self):
        obj = LearningObjective(self.xml_obj)

        assert obj != None


    def test_learning_objective_attrs(self):
        obj = LearningObjective(self.xml_obj)

        assert obj.code == "WAY-FR"
        assert obj.description == ("solve equations or optimization problems "
                                   "through translation to a standardized "
                                   "formalism.")

        assert str(obj) == ("Learning Objective (WAY-FR: solve equations or "
                            "optimization problems through translation to a "
                            "standardized formalism.)")
