"""Controller for question and answer with Ikuta Erika"""

from models import ikutaErika


def talkAboutQuestion():
    """Function to speak with Ikuta Erika"""
    ikutaErikaTeacher = ikutaErika.IkutaErikaTeacher()
    ikutaErikaTeacher.hello()
