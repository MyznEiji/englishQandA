"""Controller for question and answer with Ikuta Erika"""

from models.robotTeacher import robotTeacher


def talkAboutQuestion():
    """Function to speak with robotTeacher"""
    teacher = robotTeacher.RobotTeacher("Robot")
    teacher.hello()
    teacher.menu()
    teacher.thankYou()
