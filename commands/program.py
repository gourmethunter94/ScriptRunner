from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse
from os import popen

class ProgramCommand:
    def __init__(self, command_dictionary, command_handles):
        self.NAME = "program"
        self.HANDLE = "p"
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
        if len(values) < 1:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        return True

    def execute_command(self, values, extra_values):
        program_path = " ".join(values)
        popen(program_path)
