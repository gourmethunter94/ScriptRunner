from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue, ScriptCommandUndefinedValue
from commands.command_template import CommandTemplate

class MinusCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("minus", "mi", command_dictionary, command_handles)
        self.finalization_exception = False

    def confirm_validity(self, values, line):
        from script_runner import DEFAULT_VARIABLES
        if len(values) > 2:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        if len(values) < 2:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        if values[1] in DEFAULT_VARIABLES:
            raise ScriptCommandInvalidValue("First value given to command on line \"" + line + "\" cannot be same as one of the default variables.")
        try:
            float(values[1])
        except:
            raise ScriptCommandInvalidValue("Second value given to command on line \"" + line + "\" should be a numeric value.")
        return True
    
    def execute_command(self, values, extra_values):
        base_value = extra_values.get(values[0])
        if base_value == None:
            raise ScriptCommandUndefinedValue("Undefined variable used to try to define value of minus function.")
        try:
            new_value = float(base_value) - float(values[1])
            extra_values.update({values[0]:new_value})
        except:
            raise ScriptCommandInvalidValue("Trying to add two non numeric values together during execution of the script.")
