from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue, ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse
from pyautogui import write

SPACE = "space"

class InputCommand:
    def __init__(self, command_dictionary, command_handles):
        self.NAME = "input"
        self.HANDLE = "i"
        if command_dictionary.get(self.NAME):
            raise ScriptCommandNameAlreadyInUse("Command name: " + self.NAME + ", already in use.")
        else:
            command_dictionary.update({self.NAME:self})
        if command_handles.get(self.HANDLE):
            raise ScriptCommandHandleAlreadyInUse("Command handle: " + self.HANDLE + ", already in use.")
        else:
            command_handles.update({self.HANDLE:self.NAME})
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