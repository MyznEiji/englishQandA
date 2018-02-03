"""Utils to display to be returned to the user on the console. """

import os
import string

import termcolor


def getTemplateDirPath():
    """
        Return the path of the template's directory.

        Returns:
            str: The template dir path.
    """

    templateDirPath = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            templateDirPath = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not templateDirPath:
        baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        templateDirPath = os.path.join(baseDir, "templates")

    return templateDirPath


def findTemplate(tempFile):
    """
        Find for template file in the given location.

        Returns:
            str: The template file path

        Raises:
            NoTemplateError: If the file does not exists.
    """

    templateDirPath = getTemplateDirPath()
    tempFilePath = os.path.join(templateDirPath, tempFile)
    if not os.path.exists(tempFilePath):
        raise NoTemplateError("Could not find {}".format(tempFile))
    return tempFilePath


def getTemplate(templateFilePath, color=None, onColor=None):
    """
        Return the path of the template.

        Args:
            templateFilePath (str): The template file path
            color (str): Color formatting for output in terminal
                See in more details: https://pypi.python.org/pypi/termcolor

        Returns:
            string.Template: Return templates with characters in templates.
    """

    template = findTemplate(templateFilePath)
    with open(template, "r") as templateFile:
        contents = templateFile.read()
        contents = contents.rstrip("\n")
        contents = "\n\n{splitter}\n{contents}\n{splitter}\n\n\n".format(
            contents=contents, splitter="=" * 60)
        contents = termcolor.colored(contents, color, on_color=onColor)
        return string.Template(contents)
