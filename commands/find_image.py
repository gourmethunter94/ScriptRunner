from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue
from commands.command_template import CommandTemplate
from pyautogui import position, screenshot
from cv2 import imread, matchTemplate, TM_CCOEFF_NORMED
from numpy import unravel_index
from os import remove

class FindImageCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("findimage", "fi", command_dictionary, command_handles)
        self.finalization_exception = False

    def confirm_validity(self, values, line):
        from script_runner import DEFAULT_VARIABLES
        if len(values) > 3:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        if len(values) < 3:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        if values[0] in DEFAULT_VARIABLES:
            raise ScriptCommandInvalidValue("First value given to command on line \"" + line + "\" cannot be same as one of the default variables.")
        if values[1] in DEFAULT_VARIABLES:
            raise ScriptCommandInvalidValue("Second value given to command on line \"" + line + "\" cannot be same as one of the default variables.")
        return True
    
    def execute_command(self, values, extra_values):
        image = imread(values[2])
        screenshot().save(r'__temporary_ScriptRunner_search_image__.png')
        template = imread(r'__temporary_ScriptRunner_search_image__.png')  
        result = matchTemplate(image, template, TM_CCOEFF_NORMED)
        remove(r'__temporary_ScriptRunner_search_image__.png')
        mouse_y, mouse_x = unravel_index(result.argmax(), result.shape)
        extra_values.update({values[0]:float(mouse_x)})
        extra_values.update({values[1]:float(mouse_y)})