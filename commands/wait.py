from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue
from time import sleep
from commands.command_template import CommandTemplate

class WaitCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("wait", "w", command_dictionary, command_handles)
        self.finalization_exception = False
    
    def confirm_validity(self, values, line):
        if len(values) > 1:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        try:
            if values[0][0] != "$":
                float(values[0])
        except:
            raise ScriptCommandInvalidValue("Value given to command on line \"" + line + "\" should be either variable, integer or float.")
        return True

    def execute_command(self, values, extra_values):
        sleep(float(values[0]))
