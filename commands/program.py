from commands.errors import ScriptCommandIncorrectValueCount
from os import popen
from commands.command_template import CommandTemplate

class ProgramCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("program", "p", command_dictionary, command_handles)
        self.finalization_exception = False
    
    def confirm_validity(self, values, line):
        if len(values) < 1:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        return True

    def execute_command(self, values, extra_values):
        program_path = " ".join(values)
        popen(program_path)
