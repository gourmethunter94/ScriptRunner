from commands.errors import ScriptCommandIncorrectValueCount
from os import system
from threading import Thread
from commands.command_template import CommandTemplate

class CommandCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("command", "c", command_dictionary, command_handles)
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
