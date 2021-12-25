from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue, ScriptCommandUndefinedValue
from pyautogui import click, moveTo, position
from commands.command_template import CommandTemplate

class MouseCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("mouse", "m", command_dictionary, command_handles)
        self.buttons = {
            0:"left",
            1:"right",
            2:"middle"
        }
        self.finalization_exception = False
    
    def confirm_validity(self, values, line):
        if len(values) < 3:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        if len(values) > 3:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        try:
            int(values[0])
            if self.buttons.get(int(values[0])) == None:
                raise ScriptCommandInvalidValue("First value given to command on line \"" + line + "\" should be \"0\", \"1\", or \"2\".")
            else:
                values[0] = self.buttons.get(int(values[0]))
            if values[1][0] != "$":
                int(values[1])
            if values[2][0] != "$":
                int(values[2])
        except:
            raise ScriptCommandInvalidValue("All three values given to command on line \"" + line + "\" should be either integers.")
        return True
    
    def execute_command(self, values, extra_values):
        from script_runner import RETURN_TO_OLD_POSITION
        old_position = position()
        click(button=values[0] , x = int(values[1]), y = int(values[2]))
        if extra_values.get(RETURN_TO_OLD_POSITION):
            moveTo(old_position)