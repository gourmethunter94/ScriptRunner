from commands.errors import ScriptCommandIncorrectValueCount, ScriptCommandInvalidValue, ScriptInvalidScriptType, ScriptCommandHandleAlreadyInUse, ScriptCommandNameAlreadyInUse

class ExecuteCommand:
    def __init__(self, command_dictionary, command_handles):
        self.NAME = "execute"
        self.HANDLE = "e"
        if command_dictionary:
            if command_dictionary.get(self.NAME):
                raise ScriptCommandNameAlreadyInUse("Command name: " + self.NAME + ", already in use.")
            else:
                command_dictionary.update({self.NAME:self})
        if command_handles:
            if command_handles.get(self.HANDLE):
                raise ScriptCommandHandleAlreadyInUse("Command handle: " + self.HANDLE + ", already in use.")
            else:
                command_handles.update({self.HANDLE:self.NAME})
        self.finalization_exception = True
    
    def confirm_validity(self, values, line):
        if len(values) > 1:
            raise ScriptCommandIncorrectValueCount("Too many values given to command on line \"" + line + "\". The given path to the executable can not contain spaces.")
        return True
    
    def translation_finalization_exception(self, values, block, line):
        from script_translator import ScriptTranslator, Command, EXECUTABLE
        executable_script = Script(values[0])
        if executable_script.identifier != EXECUTABLE:
            raise ScriptInvalidScriptType("Executable script on line \"" + line + "\" is not of type \"" + EXECUTABLE + "\".")
        executable_translation = ScriptTranslator(executable_script)
        block.append(Command(command, executable_translation))

    def execute_command(self, values, extra_values):
        from script_runner import ScriptRunner
        executable_runner = ScriptRunner(values)
        executable_runner.run()