from commands.errors import ScriptCommandIncorrectValueCount, ScriptInvalidScriptType
from time import sleep
from commands.command_template import CommandTemplate

class BindCommand(CommandTemplate):
    def __init__(self, command_dictionary, command_handles):
        super().__init__("bind", "b", command_dictionary, command_handles)
    
    def confirm_validity(self, values, line, blocks):
        from script import Script
        from script_translator import EXECUTABLE
        from script_translator import ScriptTranslator
        if len(values) < 2:
            raise ScriptCommandIncorrectValueCount("Too few values given to command on line \"" + line + "\".")
        if len(values) > 2:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\".")
        executable_script = Script(values[1])
        if executable_script.identifier != EXECUTABLE:
            raise ScriptInvalidScriptType("Executable script on line \"" + line + "\" is not of type \"" + EXECUTABLE + "\".")
        executable_translation = ScriptTranslator(executable_script)
        blocks.append([values[0], executable_translation])
        return True