"""Controller for question and answer with Ikuta Erika"""

from models import idolTeacher


def talkAboutQuestion():
    """Function to speak with Ikuta Erika"""
    ikutaErikaTeacher = idolTeacher.IdolTeacher("生田絵梨花")
    ikutaErikaTeacher.hello()
    # ikutaErikaTeacher.previousGrades()
    # ikutaErikaTeacher.showQuestionsList()
    # ikutaErikaTeacher.englishQuestionsStart()
    ikutaErikaTeacher.writeQuestion()
