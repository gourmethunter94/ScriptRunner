from commands.errors import ScriptCommandIncorrectValueCount, ScriptInvalidScriptType, ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse
from time import sleep

class BindCommand:
    def __init__(self, command_dictionary, command_handles):
        self.NAME = "bind"
        self.HANDLE = "b"
        if command_dictionary.get(self.NAME):
            raise ScriptCommandNameAlreadyInUse("Command name: " + self.NAME + ", already in use.")
        else:
            command_dictionary.update({self.NAME:self})
        if command_handles.get(self.HANDLE):
            raise ScriptCommandHandleAlreadyInUse("Command handle: " + self.HANDLE + ", already in use.")
        else:
            command_handles.update({self.HANDLE:self.NAME})
    
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