from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse
from os import system
from threading import Thread

class CommandCommand:
    def __init__(self, command_dictionary, command_handles):
        self.NAME = "command"
        self.HANDLE = "c"
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
        command_string = " ".join(values)
        Thread(target=self._command_thread, args=(command_string,)).start()
    
    def _command_thread(self, command_string):
        print("    Starting thread for command: " + command_string)
        system(command_string)
        print("    Thread run completed for command: " + command_string)
