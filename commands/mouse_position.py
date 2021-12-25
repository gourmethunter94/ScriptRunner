from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue
from commands.command_template import CommandTemplate
from pyautogui import position

class MousePositionCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("mouseposition", "mp", command_dictionary, command_handles)
        self.finalization_exception = False

    def confirm_validity(self, values, line):
        from script_runner import DEFAULT_VARIABLES
        if len(values) > 2:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        if len(values) < 2:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        if values[0] in DEFAULT_VARIABLES:
            raise ScriptCommandInvalidValue("First value given to command on line \"" + line + "\" cannot be same as one of the default variables.")
        if values[1] in DEFAULT_VARIABLES:
            raise ScriptCommandInvalidValue("Second value given to command on line \"" + line + "\" cannot be same as one of the default variables.")
        return True
    
    def execute_command(self, values, extra_values):
        mouse_x, mouse_y = position()
        extra_values.update({values[0]:float(mouse_x)})
        extra_values.update({values[1]:float(mouse_y)})
