from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue, ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse
from time import sleep

class WaitCommand:
    def __init__(self, command_dictionary, command_handles):
        self.NAME = "wait"
        self.HANDLE = "w"
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
        try:
            float(values[0])
        except:
            raise ScriptCommandInvalidValue("Value given to command on line \"" + line + "\" should be either integer or float.")
        return True
    
    def execute_command(self, values, extra_values):
        sleep(float(values[0]))
