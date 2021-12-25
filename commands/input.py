from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue
from pyautogui import write
from commands.command_template import CommandTemplate

SPACE = "space"

class InputCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("input", "i", command_dictionary, command_handles)
        self.finalization_exception = False
    
    def confirm_validity(self, values, line):
        if len(values) > 1:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        if values[0] == SPACE:
            values[0] = " "
        if len(values[0]) > 1:
            raise ScriptCommandInvalidValue("Value given to command on line \"" + line + "\" should be singular keyboard character.")
        return True

    def execute_command(self, values, extra_values):
        write(str(values[0]))