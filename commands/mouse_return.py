from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue
from commands.command_template import CommandTemplate

class MouseReturnCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("mousereturn", "mr", command_dictionary, command_handles)
        self.finalization_exception = False
    
    def confirm_validity(self, values, line):
        if len(values) > 1:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        try:
            if int(values[0]) < 0 or int(values[0]) > 1:
                raise ScriptCommandInvalidValue("Value given to command on line \"" + line + "\" should be \"0\" or \"1\".")
        except:
            raise ScriptCommandInvalidValue("Value given to command on line \"" + line + "\" should be either integer or float.")
        return True
    
    def execute_command(self, values, extra_values):
        from script_runner import RETURN_TO_OLD_POSITION
        extra_values.update({RETURN_TO_OLD_POSITION:bool(int(values[0]))})
