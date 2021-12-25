from commands.errors import ScriptCommandIncorrectValueCount
from commands.command_template import CommandTemplate

class EscapeKeyCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("escapekey", "ek", command_dictionary, command_handles)
        self.finalization_exception = False
    
    def confirm_validity(self, values, line):
        if len(values) > 1:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        return True
    
    def execute_command(self, values, extra_values):
        from script_runner import ESCAPE_KEY
        extra_values.update({ESCAPE_KEY:values[0]})
